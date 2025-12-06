from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import PlainTextResponse
from starlette.responses import JSONResponse
from models import Book, BookResponse
import json

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return {
        "book_id": book_id,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald"
    }

@app.get("/authors/{author_id}")
async def read_author(author_id: int):
    return {
        "author_id": author_id,
        "name": "Ernest Hemingway"
    }

@app.get("/books")
async def read_books(year: int = None):
    if year:
        return {
            "year": year,
            "books": ["Book 1", "Book 2"]
        }
    return {"books": ["All Books"]}

@app.get("/allbooks")
async def read_all_books() -> list[BookResponse]:
    return [
        {"id": 1, "title": "Machine Learning", "author": "Chip Huyen"},
        {"Id": 2, "title": "Computer Vision", "author": "Kaparthy"}
    ]

@app.post("/book")
async def create_book(book: Book):
    return book

@app.get("/error_endpoint")
async def raise_exception():
    raise HTTPException(status_code=400)

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": "OOPs ! Something went wrong"
        }
    )

@app.exception_handler(ResponseValidationError)
async def validation_exception_handler(
    request: Request ,
    exc: ResponseValidationError
):
    return PlainTextResponse(
        "This is a plain text response:"
        f"\n{json.dumps(exc.errors(), indent=2)}",
        status_code=status.HTTP_400_BAD_REQUEST
    )
