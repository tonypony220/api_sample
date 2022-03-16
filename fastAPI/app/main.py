from fastapi import Depends, FastAPI, HTTPException, Header
from sqlalchemy.orm import Session
import uvicorn
import crud, schemas, models
from database import engine, SessionLocal

from fastapi_pagination import Page, add_pagination, paginate


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Scan
@app.post("/scan/get", response_model=Page[schemas.Scan], summary="Retrieve a list of scans",
          description="Retrieve a list of scans")
async def get_scan(db: Session = Depends(get_db)):  # X_User_Id: str = Header(...), X_Org_Id: str = Header(...),
    scan = crud.get_scan(db)
    return paginate(scan)


@app.get("/scan/range", response_model=Page[schemas.Scan], summary="Retrieve a list of scans by ID range",
         description="Retrieve a list of scans by")
async def get_range_scan(offset: int, limit: int, db: Session = Depends(get_db)):
    scan = crud.get_range_scan(db, offset=offset, limit=limit)
    return paginate(scan)


@app.get("/scan/getById/{id}/", response_model=schemas.Scan, summary="Retrieve a scan by ID",
         description="Retrieve a scan by ID")
async def get_byid_scan(id: int, db: Session = Depends(get_db)):
    scan = crud.get_byid_scan(db, scan_id=id)
    return scan


# Identity

# @app.post("/create_identity/", response_model=schemas.Identity)
# def create_identity(identity: schemas.IdentityCreate, db: Session = Depends(get_db)):
#     db_entry = crud.get_byid_identity(db, identity_id=identity.id)
#     if db_entry:
#         raise HTTPException(status_code=400, detail="Entry with this id already exists")
#     return crud.create_identity(db=db, identity=identity)


@app.post("/identity/get", response_model=Page[schemas.Identity], summary="Retrieve a list of identities",
          description="Retrieve a list of identities")
async def get_identity(db: Session = Depends(get_db)):  # , X_User_Id: str = Header(...), X_Org_Id: str = Header(...)):
    identity = crud.get_identity(db)
    return paginate(identity)


@app.get("/identity/range", response_model=Page[schemas.Identity], summary="Retrieve a list of identities by ID range",
         description="Retrieve a list of identities by")
async def get_range_identity(offset: int, limit: int, db: Session = Depends(get_db)):
    identity = crud.get_range_identity(db, offset=offset, limit=limit)
    return paginate(identity)


@app.get("/identity/getById/{id}/", response_model=schemas.Identity, summary="Retrieve an identity by ID",
         description="Retrieve an identity by ID")
async def get_byid_identity(id: int, db: Session = Depends(get_db)):
    identity = crud.get_byid_identity(db, identity_id=id)
    return identity


add_pagination(app)

if __name__ == '__main__':
    uvicorn.run('api:app', host='0.0.0.0', port=80)
