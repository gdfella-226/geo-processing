""" SQL queries for database

"""
COMMANDS = {
    "drop": "DROP TABLE IF EXISTS %s;".replace("'", ""),
    "show": "SELECT * FROM %s",
    'tables': """SELECT table_name FROM information_schema.tables WHERE table_schema NOT IN
     ('information_schema', 'pg_catalog') AND table_schema IN('public');"""
}


def drop(table):
    return f"DROP TABLE IF EXISTS {table};"


def insert(table, content):
    query = f"INSERT INTO {table} VALUES"
    for line in content:
        query += f'''('{"', '".join(line)}'),'''
    return query[:-1] + ';'


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


def create(name, columns: list):
    """
    Generates 'CREATE' SQL command
    :param name: table name
    :param columns: list of columns names
    :return: str
    """
    type_param = 'VARCHAR(255)'
    columns_specification = \
        ', '.join([f'"{column_name}" {type_param}' for column_name in columns])
    return f'CREATE TABLE {name}({columns_specification})'
