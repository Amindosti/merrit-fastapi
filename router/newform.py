from fastapi import APIRouter, Depends, HTTPException, status
import database, models, schemas
from sqlalchemy.orm import Session

get_db = database.get_db


router = APIRouter(
    prefix='/newform',
    tags=['form']
)


@router.post('/')
async def create_new_form(request: schemas.Form, db: Session = Depends(get_db)):
    new_form = models.NewForm(author=request.Author, Form=request.Form,
                              Form_name=request.Form_Name, Privacy=request.Privacy)
    db.add(new_form)
    db.commit()
    db.refresh(new_form)
    return HTTPException(status_code=status.HTTP_201_CREATED)


@router.get('/form')
async def send_all_form(db: Session = Depends(get_db)):
    form = db.query(models.NewForm).all()
    return form
