import netCDF4 as nc
import numpy as np
import math
from DBcreate import Lightning, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from netCDF4 import Dataset
import sys
import os

engine = create_engine('sqlite:///sqlalchemy.db')
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

# light = session.query(Lightning)\
#     .filter(Lightning.time == '20-09-25T07:00:00.000Z') \
#     .filter(Lightning.lat == '41.54070675583593')\
#     .filter(Lightning.lon == '13.12419891357423')\
#     .count()
#
# print(light)
# session.commit()

if len(sys.argv) < 2:
    print('usage: DBquery.py inputPath/ outputPath/')
    exit(1)

for item in os.listdir(sys.argv[1]):
    if item.endswith(".nc4"):
        date = item[-20:-9]

        year = date[2:4]
        month = date[4:6]
        day = date[6:8]
        hour = date[9:]

        newDate = year + '-' + month + '-' + day + 'T' + hour
        # date = sys.argv[1]  # YY-MM-DDT00:00
        newDate = newDate + ':00:00.000Z'
        print(newDate)
        print(item)

        with nc.Dataset(sys.argv[1] + item, format="NETCDF4") as src, nc.Dataset(sys.argv[2] + item,
                                                                                 'w', format="NETCDF4") as dst:
            # copy global attributes all at once via dictionary
            dst.setncatts(src.__dict__)
            # copy dimensions
            for name, dimension in src.dimensions.items():
                dst.createDimension(
                    name, (len(dimension) if not dimension.isunlimited() else None))
            # copy all file data except for the excluded
            for name, variable in src.variables.items():
                # if name not in toexclude:
                x = dst.createVariable(name, variable.datatype, variable.dimensions)
                dst[name][:] = src[name][:]
                # copy variable attributes all at once via dictionary
                dst[name].setncatts(src[name].__dict__)

        model = Dataset(sys.argv[2] + item, "r+", format="NETCDF4")

        x = model.createVariable('X', 'i4', ('longitude',))
        y = model.createVariable('Y', 'i4', ('latitude',))

        x[:] = np.arange(0, 543)
        y[:] = np.arange(0, 553)

        # model.createDimension('t', 1)
        #
        # lats = model.createVariable('lat', 'f4', ('X', 'Y'))
        # lats.units = 'degree_north'
        # lats._CoordinateAxisType = 'Lat'
        #
        # lons = model.createVariable('lon', 'f4', ('X', 'Y'))
        # lons.units = 'degree_east'
        # lons._CoordinateAxisType = 'Lon'

        lightCounter = model.createVariable('light', 'i4', ('time', 'latitude', 'longitude'))

        deltaLat = (model['latitude'][1] - model['latitude'][0])
        deltaLon = (model['longitude'][1] - model['longitude'][0])

        lightMat = np.full([len(model['latitude']), len(model['longitude'])], 0, dtype=np.int)

        # for j in range(0, 553):
        #     for i in range(0, 543):
        #         cLat = (model['latitude'][j])
        #         cLon = (model['longitude'][i])
        #         center = (cLat, cLon)
        #
        #         minLon = center[1] - deltaLon / 2
        #         minLat = center[0] - deltaLat / 2
        #         maxLon = center[1] + deltaLon / 2
        #         maxLat = center[0] + deltaLat / 2
        #
        #         minC = (minLat, minLon)
        #         maxC = (maxLat, maxLon)
        #
        #         # light = session.query(Lightning) \ .filter(Lightning.time == '20-08-01T04:00:00.000Z') \
        #         #     .count()
        #
        #         light = session.query(Lightning) \
        #             .filter(Lightning.time == newDate) \
        #             .filter(Lightning.lat.between(minLat, maxLat)) \
        #             .filter(Lightning.lon.between(minLon, maxLon)) \
        #             .count()
        #
        #         lightMat[j][i] = light
        #
        #         # if light != 0: break
        #         del light
        #
        # lightCounter[0, :, :] = lightMat
        # count = 0
        # for i in range(len(lightMat[:, 0])):
        #     for j in range(len(lightMat[0, :])):
        #         if lightMat[i][j] != 0:
        #             print(str(i) + ' ' + str(j))
        #             count += 1
        # print(count)

        model.close()
