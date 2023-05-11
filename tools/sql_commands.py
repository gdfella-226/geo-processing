""" SQL queries for database

"""
COMMANDS = {
    "drop": """DROP TABLE IF EXISTS data;""",
    "show": """SELECT * FROM data""",
    'insert': f'INSERT INTO data VALUES ({",".join(["%s"] * 25)})'
}


def exists(table):
    """
        Generates SQL command that return true if table exists
        :param table: table name
        :return: str
    """
    return f"""SELECT EXISTS (
        SELECT * FROM 
            public.tables
        WHERE
            tablename  = 'data'
        );"""


def create(columns: list):
    """
    Generates 'CREATE' SQL command
    :param columns: list of columns names
    :return: str
    """
    type_param = 'VARCHAR(255)'
    columns_specification = \
        ', '.join([f'"{column_name}" {type_param}' for column_name in columns])
    return f'CREATE TABLE data ({columns_specification})'
