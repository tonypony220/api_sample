from sqlalchemy.orm import Session
import models


# Scan
def get_byid_scan(db: Session, scan_id: int):
    return db.query(models.Scan).filter(models.Scan.id == scan_id).first()


def get_range_scan(db: Session, offset: int, limit: int):
    query = db.query(models.Scan).offset(offset).limit(limit).all()
    return query


def get_scan(db: Session):
    return db.query(models.Scan).all()


# Identity
def get_byid_identity(db: Session, identity_id: int):
    return db.query(models.Identity).filter(models.Identity.id == identity_id).first()


def get_range_identity(db: Session, offset: int, limit: int):
    query = db.query(models.Identity).offset(offset).limit(limit).all()
    return query


def get_identity(db: Session):
    return db.query(models.Identity).all()


# def create_identity(db: Session, identity: schemas.IdentityCreate):
#     db_entry = models.Identity(id=identity.id, UID=identity.UID, UserID=identity.UserID,
#                                LicenseNumber=identity.LicenseNumber, OrgID=identity.OrgID)
#     db.add(db_entry)
#     db.commit()
#     db.refresh(db_entry)
#     return db_entry
