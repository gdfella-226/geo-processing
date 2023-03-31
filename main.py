import argparse
from DBHandler import DBHandler


def parse():
    parser = argparse.ArgumentParser(description='Convert XLSX file to PostgreSQL database')
    parser.add_argument('-f', '--filename', type=str, help='Path to XLSX file for read')
    parser.add_argument('-d', '--database', type=str, help='PostgreSQL database name')
    parser.add_argument('-u', '--user', type=str, help='User name')
    parser.add_argument('-ps', '--password', type=str, help='Password')
    parser.add_argument('-ht', '--host', type=str, help='Host')
    parser.add_argument('-p', '--port', type=str, help='Port')

    return parser.parse_args()


def main():
    db = DBHandler(parse())
    db.create_table()
    db.fill_table()
    #db.show_table()


if __name__ == "__main__":
    main()
