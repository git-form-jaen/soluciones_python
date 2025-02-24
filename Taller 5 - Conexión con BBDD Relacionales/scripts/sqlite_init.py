import os
import sqlite3

# Conectar a SQLite y crear la base de datos y tabla
os.makedirs("database", exist_ok=True)
conn_sqlite = sqlite3.connect("database/zprinter.db")
cursor_sqlite = conn_sqlite.cursor()

cursor_sqlite.execute("DROP TABLE IF EXISTS orders;")  # Elimina la tabla si ya existe
cursor_sqlite.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    client_id INTEGER,
    status TEXT,
    last_updated TEXT
);
""")

# Insertar más registros que en MySQL
pedidos_iniciales = [
    (1, 100, "Pendiente de pago", "2024-04-01 10:00:00"),  # Ya existe en MySQL
    (2, 101, "En proceso", "2024-04-02 11:30:00"),        # Ya existe en MySQL
    (3, 102, "Enviado", "2024-04-03 12:45:00"),          # Nuevo (no está en MySQL)
    (4, 103, "Enviado", "2024-04-04 09:20:00"),          # Nuevo
    (5, 104, "En proceso", "2024-04-05 16:15:00"),       # Nuevo
    (6, 105, "Cancelado", "2024-04-06 14:10:00"),        # Nuevo
    (7, 106, "Pendiente de pago", "2024-04-07 18:00:00") # Nuevo
]

cursor_sqlite.executemany(
    "INSERT INTO orders (order_id, client_id, status, last_updated) VALUES (?, ?, ?, ?);",
    pedidos_iniciales
)
conn_sqlite.commit()
cursor_sqlite.close()
conn_sqlite.close()

print("Base de datos SQLite creada.")
