from fastapi import APIRouter, Depends, HTTPException, status
import database, models, schemas
from sqlalchemy.orm import Session

get_db = database.get_db


router = APIRouter(
    prefix='/dataentry',
    tags=['dataentry']
)


@router.post('/')
async def data_entry(request: schemas.Data, db: Session = Depends(get_db)):
    new_form_data = models.DataEntry(writer=request.writer, formId=request.formId,
                                   answer=request.answer)
    db.add(new_form_data)
    db.commit()
    db.refresh(new_form_data)
    return HTTPException(status_code=status.HTTP_201_CREATED)


@router.get('/answers')
async def send_all_answers(db: Session = Depends(get_db)):
    answers = db.query(models.DataEntry).all()
    return answers
