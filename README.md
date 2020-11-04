# weather-lightning
A tool for the extraction of lightning data, used to improve meteorological predictions (http://data.meteo.uniparthenope.it/opendap/opendap/) via Machine learning.

# Installation

#### Clone the repository and create the virtual enviroment for Python 3
```console
$ git clone https://github.com/salvatorenanni/weather-lightning.git
$ cd weather-lightning
$ virtualenv venv
```
#### Activate the environment
```console
$ source venv/bin/activate
```
#### Install requirements
```console
$ pip install -r requirements.txt
```

# Usage

The repository gives access to two folders in which are divided the scripts, designed to extract and create a csv file, with the aim of use the latter as a Machine Learning dataset.

The scripts are designed to work as follows:
```console
python3 DBcreate.py
python3 main.py
python3 DBquery.py
python3 csvReader.py
(optional) python3 circle.py //filters the dataset
```
W.I.P.
