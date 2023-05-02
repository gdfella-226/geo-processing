""" SQL queries for database

"""
COMMANDS = {
    "drop": """DROP TABLE IF EXISTS data;""",
    "show": """SELECT * FROM data""",
    "insert": """INSERT INTO data VALUES (
          %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
}


def create(columns: list):
    prefix = "CREATE TABLE data ("
    for i in columns:
        prefix += f"\"{i}\" VARCHAR(255), "
    prefix = prefix[:-2]
    prefix += ")"
    print(prefix)
    return prefix
