from pydantic import BaseModel


class ScanBase(BaseModel):
    id: int
    value: str


class ScanCreate(ScanBase):
    pass


class Scan(ScanBase):
    id: int
    value: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": "1",
                "value": "green",
            }
        }


class IdentityBase(BaseModel):
    id: int
    UID: int
    UserID: str
    LicenseNumber: str = None
    OrgID: str = None


class IdentityCreate(IdentityBase):
    pass


class Identity(IdentityBase):
    id: int
    UID: int
    UserID: str
    LicenseNumber: str = None
    OrgID: str = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": "1",
                "UID": "1",
                "UserID": "1",
                "LicenseNumber": "S76743537721",
                "OrgID": "1",
            }
        }
