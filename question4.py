import json
import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
JSON_FILE = BASE_DIR / "appendix_a.json"
DB_FILE = BASE_DIR / "production_files.db"


def load_json(path):
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("Top-level JSON value must be a list")

    return data


def create_schema(connection):
    connection.execute("PRAGMA foreign_keys = ON")

    connection.execute("""
        CREATE TABLE IF NOT EXISTS nodes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            parent_id INTEGER,
            type TEXT NOT NULL CHECK(type IN ('folder', 'file')),
            name TEXT NOT NULL,
            path TEXT NOT NULL UNIQUE,
            FOREIGN KEY(parent_id) REFERENCES nodes(id) ON DELETE CASCADE
        )
    """)

    connection.execute("""
        CREATE INDEX IF NOT EXISTS idx_nodes_parent_id
        ON nodes(parent_id)
    """)


def insert_node(connection, node, parent_id=None, parent_path=""):
    node_type = node.get("type")
    name = node.get("name")

    if node_type not in {"folder", "file"}:
        raise ValueError(f"Unsupported node type: {node_type!r}")

    if not isinstance(name, str) or not name:
        raise ValueError("Every node must have a non-empty name")

    path = f"{parent_path}/{name}" if parent_path else name

    cursor = connection.execute(
        """
        INSERT INTO nodes (parent_id, type, name, path)
        VALUES (?, ?, ?, ?)
        """,
        (parent_id, node_type, name, path),
    )

    node_id = cursor.lastrowid

    children = node.get("children", [])

    if node_type == "file" and children:
        raise ValueError(f"File cannot contain children: {path}")

    for child in children:
        insert_node(
            connection,
            child,
            parent_id=node_id,
            parent_path=path,
        )


def build_database(data, db_path=DB_FILE):
    # Recreate the database so repeated runs always produce the same result.
    if db_path.exists():
        db_path.unlink()

    with sqlite3.connect(db_path) as connection:
        create_schema(connection)

        with connection:
            for node in data:
                insert_node(connection, node)

    return db_path


def print_database(db_path):
    with sqlite3.connect(db_path) as connection:
        rows = connection.execute(
            """
            SELECT id, parent_id, type, name, path
            FROM nodes
            ORDER BY id
            """
        ).fetchall()

    for row in rows:
        print(row)


if __name__ == "__main__":
    data = load_json(JSON_FILE)
    database = build_database(data)

    print(f"SQLite database created: {database}")
    print_database(database)
