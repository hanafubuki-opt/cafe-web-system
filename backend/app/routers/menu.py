from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models

router = APIRouter(prefix="/menu", tags=["menu"])

@router.get("/", response_model=list[dict])
def list_menu(db: Session = Depends(get_db)):
    items = db.query(models.MenuItem).all()
    return [{"id": i.id, "name": i.name, "price": i.price} for i in items]
