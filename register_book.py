def register_book(title, author, isbn, total_pages, genre="Desconocido"):
    if not title or not author or not isbn or total_pages <= 0:
        return "Error: Datos incompletos o inválidos."

    existing_books = ["9788437604947", "9788446025726"]

    if isbn in existing_books:
        return "Error: Este ISBN ya está registrado."

    new_book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "total_pages": total_pages,
        "genre": genre
    }

    print(f"Libro registrado exitosamente: {new_book}")
    return "Success"


# Ejemplo de prueba
print(register_book("Rayuela", "Julio Cortázar", "9788437604947", 600, "Novela"))
print(register_book("Cien años de soledad", "Gabriel García Márquez", "9780307474728", 417, "Realismo mágico"))
