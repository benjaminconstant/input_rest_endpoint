import models, schemas
from sqlalchemy.orm import Session

def create_item(item: schemas.Item, db: Session):
    db_item = models.Item(correlationId=item.correlationId, src=item.src)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)