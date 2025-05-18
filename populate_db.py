from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

# Cria as tabelas no banco (caso ainda não existam)
models.Base.metadata.create_all(bind=engine)

# Lista de livros de exemplo
sample_books = [
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
]

# Cria uma sessão com o banco
db: Session = SessionLocal()

# Adiciona os livros
for book in sample_books:
    db_book = models.Book(**book)
    db.add(db_book)

# Salva no banco e fecha a sessão
db.commit()
db.close()

print("Sample books inserted successfully!")
