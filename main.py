from fastapi import FastAPI, Depends, HTTPException
import schemas, models, utils
from database import engine
from sqlalchemy.orm import Session
from database import get_db

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

@app.post('/b64/', status_code=201)
async def post_b64(item: schemas.Item, db: Session = Depends(get_db)):
    try:
        return utils.process_item(item, db)
    except Exception as e:
        if isinstance(e, HTTPException):
            raise e
        else:
            raise HTTPException(status_code=503, detail="Internal Error")