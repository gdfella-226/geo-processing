"""App for visualize geographic data

"""
import argparse
from tools.db_handler import DBHandler


def parse():
    """Function for parsing user's parameters

    Returns:
        Namespace: Arguments passed in code by values of flags

    """
    parser = argparse.ArgumentParser(description='Convert XLSX file to PostgreSQL database')
    parser.add_argument('-f', '--filename', type=str, help='Path to XLSX file for read',
                        required=True)
    parser.add_argument('-d', '--database', type=str, help='PostgreSQL database name')
    parser.add_argument('-u', '--user', type=str, help='User name')
    parser.add_argument('-ps', '--password', type=str, help='Password')
    parser.add_argument('-ht', '--host', type=str, help='Host')
    parser.add_argument('-p', '--port', type=str, help='Port')
    parser.add_argument('-o', '--overwrite', action='store_true',
                        help='Provides ability to overwrite new data instead of appending. \
                             Use program without -o only if you sure that database already exists!')

    return parser.parse_args()


def main():
    """Main function starts the app

    """
    args = parse()
    base = DBHandler(args)
    base.create_table()
    base.fill_table()
    base.show_table()


if __name__ == "__main__":
    main()
