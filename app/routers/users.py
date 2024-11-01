from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session, joinedload
from typing import Annotated
from .. import models, schemas, database, exceptions, oauth2, security


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

session_dep = Annotated[Session, Depends(database.get_db)]
user_id_dep = Annotated[int, Depends(oauth2.get_current_user_id)]


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[schemas.Users])
def get_users(session: session_dep, user_id: user_id_dep, limit: int = 10):
    users = session.query(models.User).limit(limit).all()
    return users


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.User)
def get_user(id: int, session: session_dep):
    user = session.get(models.User, id)
    if user is None: raise exceptions.resource_not_found
    return user


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.User)
def register_user(user: schemas.UserRegister, session: session_dep):
    existing_user = session.query(models.User).filter_by(email=user.email).one_or_none()
    if existing_user: raise exceptions.duplicate_email

    # hashed_password = security.get_hashed_password(user.password)
    user.password = security.get_hashed_password(user.password)
    new_user = models.User(**user.model_dump())
    session.add(new_user)
    session.commit()
    return new_user


@router.delete("/deletion", status_code=status.HTTP_204_NO_CONTENT)
def graduate_user(session: session_dep, user_id: user_id_dep):
    user_to_graduate = session.get(models.User, user_id)
    session.delete(user_to_graduate)
    session.commit()
    return {"detail": "User successfully graduated."}
