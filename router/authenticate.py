from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import models
import database
from . import Token
from hashing import Hash


router = APIRouter(
    tags=['Authentication']
)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(),
          db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.name == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='user not found')
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='password is incorrect!')

    access_token = Token.create_access_token(data={"sub": user.name})
    return {"access_token": access_token, "token_type": "bearer"}
