from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Annotated
from .. import models, schemas, database, exceptions, oauth2, security


router = APIRouter(
    prefix="/login",
    tags=["Login"]
)

session_dep = Annotated[Session, Depends(database.get_db)]
form_data_dep = Annotated[OAuth2PasswordRequestForm, Depends()]


@router.post("/", response_model=schemas.Token)
def login_user(session: session_dep, form_data: form_data_dep):
    user = session.query(models.User).filter_by(email=form_data.username).one_or_none()
    if (not user) or (not security.verify_password(form_data.password, user.password)):
        raise exceptions.unauthorized_access
    
    access_token = oauth2.create_access_token(user.id)
    token_type = "bearer"
    return schemas.Token(
        access_token=access_token,
        token_type=token_type
    )
