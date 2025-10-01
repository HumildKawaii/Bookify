from sqlalchemy.orm import Session
from . import models, schemas

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def get_books(db: Session, skip: int = 0, limit: int = 100, author: str = None, genre: str = None, year: int = None):
    query = db.query(models.Book)
    if author:
        query = query.filter(models.Book.author == author)
    if genre:
        query = query.filter(models.Book.genre == genre)
    if year:
        query = query.filter(models.Book.year == year)
    return query.offset(skip).limit(limit).all()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict(exclude_unset=True))
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, db_book: models.Book, book_update: schemas.BookUpdate):
    update_data = book_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_book, key, value)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, db_book: models.Book):
    db.delete(db_book)
    db.commit()
