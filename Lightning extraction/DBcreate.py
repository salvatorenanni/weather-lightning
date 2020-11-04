from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from decimal import Decimal as D
import sqlalchemy.types as types


class SqliteNumeric(types.TypeDecorator):
    impl = types.String

    def load_dialect_impl(self, dialect):
        return dialect.type_descriptor(types.VARCHAR(100))

    def process_bind_param(self, value, dialect):
        return str(value)

    def process_result_value(self, value, dialect):
        return D(value)


Numeric = SqliteNumeric
Base = declarative_base()


class Lightning(Base):
    __tablename__ = 'lightning'
    id = Column(Integer, primary_key=True)
    lat = Column(Numeric(17, 14), nullable=False)
    lon = Column(Numeric(17, 14), nullable=False)
    time = Column(String(24))


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///sqlalchemy.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
