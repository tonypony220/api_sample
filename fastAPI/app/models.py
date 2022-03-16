from sqlalchemy import Column, Integer, String

from database import Base


class Scan(Base):
    __tablename__ = "s_db"

    id = Column(Integer, primary_key=True)
    value = Column(String)


class Identity(Base):
    __tablename__ = "i_db"

    id = Column(Integer, primary_key=True)
    UID = Column(Integer)
    UserID = Column(String)
    LicenseNumber = Column(String)
    OrgID = Column(String)
