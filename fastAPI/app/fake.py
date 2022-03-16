# import main
import main
import models
# from . import models

print("creating fake data")

db = main.get_db()

for i in range(1, 10):
    db_entry = models.Identity(UID=i,
                               UserID=i * 10,
                               LicenseNumber=i * 100,
                               OrgID=i * 1000)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)

for i in range(1, 10):
    db_entry = models.Scan(value=i + 2)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
