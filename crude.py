from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


app = FastAPI()


books = [
    {
        "id": 1,
        "title":"the subtle art of not giving a fuck",
        "writer":"mark manson"
    },
     {
        "id": 2,
        "title":"the subtle art of not giving a fuck",
        "writer":"mark manson"
    },
     {
        "id": 3,
        "title":"the subtle art of not giving a fuck",
        "writer":"mark manson"
    },
     {
        "id": 4,
        "title":"the subtle art of not giving a fuck",
        "writer":"mark manson"
    },
     {
        "id": 5,
        "title":"the subtle art of not giving a fuck",
        "writer":"mark manson"
    }
]


@app.get("/books")
def get_books():
    for book in books:
        if book == []:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="no books available")
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="book not found")


class Book(BaseModel):
    id:int
    title:str
    writer:str

@app.post("/add_books")
def post_books(book: Book):
    new_book = book.model_dump()
    books.append(new_book)
    return new_book


class EditBook(BaseModel):
    title: str
    writer: str

@app.put("/edit-book/{book_id}")
def edit_book(book_id: int, book_update: EditBook):
    for book in books:
        if book["id"] == book_id:
           book['title'] = book_update.title
           book['writer'] = book_update.writer
           return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="book not found")
@app.delete("/delete-book/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "book deleted successfully"}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="book not found")