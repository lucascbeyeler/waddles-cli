from dataclasses import dataclass
from typing import TYPE_CHECKING

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base

from waddles_cli.constants.keywords import SQLALCHEMY_CONN_STRUCTURE

if TYPE_CHECKING:
    from waddles_cli.models.config import Database

Base = declarative_base()

@dataclass
class WaddlesStorageDatabase:

    database_config: Database

    def initialize(self):
        self.engine = create_engine(
            SQLALCHEMY_CONN_STRUCTURE.format(server_type=self.database_config.server_type,
                                             database_name=self.database_config.database_name))
        self.connection = self.engine.connect()
        self.sessionmaker = sessionmaker(bind=self.engine)
        self.session = self.sessionmaker()

    class MailBackup(Base):
        __tablename__ = "mail_backup"

        id = Column(Integer, primary_key=True)
        email = Column(String)
        date = Column(Date)
        size = Column(Integer)
        status = Column(String)
        session_id = relationship("SessionBackup")

    class SessionBackup(Base):

        __tablename__ = "session_backup"
        id = Column(Integer, primary_key=True)
        date = Column(Date)
        size = Column(Integer)