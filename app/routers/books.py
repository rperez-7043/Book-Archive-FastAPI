from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import Annotated
from .. import models, schemas, database, exceptions, oauth2


router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

session_dep = Annotated[Session, Depends(database.get_db)]
user_id_dep = Annotated[int, Depends(oauth2.get_current_user_id)]


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[schemas.Book])
def get_books(session: session_dep, limit: int = 10):
    books = session.query(models.Book).limit(limit).all()
    return books


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.Book)
def get_book(id: int, session: session_dep):
    book = session.get(models.Book, id)
    if book is None: raise exceptions.resource_not_found
    return book


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Book)
def publish_book(book: schemas.BookPublish, session: session_dep, user_id: user_id_dep):
    new_book = models.Book(**book.model_dump())
    session.add(new_book)
    session.commit()
    return new_book


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def withdraw_book(id: int, session: session_dep, user_id: user_id_dep):
    book_to_withdraw = session.get(models.Book, id)
    if book_to_withdraw is None: raise exceptions.resource_not_found
    
    session.delete(book_to_withdraw)
    session.commit()
    return {"detail": "Book successfully withdrawn."}
