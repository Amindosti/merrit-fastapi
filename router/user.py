from fastapi import APIRouter, Depends, HTTPException, status
import database, models, schemas
from sqlalchemy.orm import Session
from hashing import Hash


router = APIRouter(
    prefix='/user',
    tags=['user']
)
get_db = database.get_db


@router.post('/signup', response_model=schemas.ShowUser)
async def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name, password=Hash.bcrypt(request.password),
                           email=request.email, role=request.role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    if new_user:
        return new_user
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.get("/get")
def return_the_data_from_database(db: Session = Depends(get_db)):
    user = db.query(models.User.name, models.User.role).all()
    return user



