class Queries:
    CREATE_SURVEY_TABLE = """
        CREATE TABLE IF NOT EXISTS surveys (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone_num TEXT,
            visit TEXT,
            rate INTEGER,
            review TEXT
        )
    """