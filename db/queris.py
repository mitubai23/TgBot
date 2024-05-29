class Queries:
    CREATE_SURVEY_TABLE = """
        CREATE TABLE IF NOT EXISTS surveys (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            genre TEXT,
            rating INTEGER
        )
    """
    DROP_CATEGORY_TABLE = "DROP TABLE IF EXISTS categories"
    CREATE_CATEGORIES_TABLE = """
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """
    DROP_MEALS_TABLE = "DROP TABLE IF EXISTS meals"
    CREATE_MEALS_TABLE = """
        CREATE TABLE IF NOT EXISTS meals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            price FLOAT,
            picture TEXT,
            category_id INTEGER,
            FOREIGN KEY(category_id) REFERENCES categories(id)
        )
    """
    POPULATE_CATEGORIES = """
        INSERT INTO categories (name) VALUES
            ('Пицца'),
            ('Супы'),
            ('Роллы')
    """
    POPULATE_MEALS = """
        INSERT INTO meals (name, description, price, picture, category_id) VALUES
        ('Пеперони', 'колбаса, сыр, тесто', 790.0, 'images/peperony.jpg', 1),
        ('Том Ям', 'грибы, острый суп', 560.0, 'images/tomyam.jpg', 2),
        ('Филадельфия', 'рыба, рис, огурец', 750.0, 'images/philadelphie.jpg', 3)
    """