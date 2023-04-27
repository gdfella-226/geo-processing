"""Replace data from .xlsx file to PostgreSQL database

"""
import json
import openpyxl
import psycopg2
from loguru import logger
# pylint: disable=import-error
from tools.sql_commands import COMMANDS
# pylint: enable=import-error


class DBHandler:
    """Class for operating with DB and table

    """
    def __init__(self, args):
        self.conn = None
        self.cur = None
        with open('./data/config.json', 'r', encoding='UTF-8') as config_file:
            args_dict = vars(args)
            default_data = json.load(config_file)
            for key, val in args_dict.items():
                if not val:
                    args_dict[key] = default_data[key]
            self.config_data = args_dict
        logger.info(f'Connecting with params: {self.config_data}.....')

        self.connect()

    def read_xlsx(self):
        """Reads data from .xlsx file

        Returns:
            list: data from .xlsx in python's list of lists

        """
        workbook = openpyxl.load_workbook(self.config_data["filename"])
        worksheet = workbook.active
        table = [[] for i in range(worksheet.max_row)]
        for row in range(1, worksheet.max_row):
            for cell in worksheet[row]:
                if cell.value and cell.value != '':
                    table[row].append(cell.value)
                else:
                    table[row].append(None)

        for i in table:
            if not i:
                table.remove(i)
        try:
            int(table[0][0])
        except ValueError:
            table.pop(0)
        return table

    def connect(self):
        """Connect to postgres database

        """
        logger.info("Connecting to DB....")
        try:
            self.conn = psycopg2.connect(database=self.config_data["database"],
                                         user=self.config_data["user"],
                                         password=self.config_data["password"],
                                         host=self.config_data["host"],
                                         port=self.config_data["port"])
            self.cur = self.conn.cursor()
            logger.info("Success!")
        except psycopg2.DatabaseError as error:
            logger.info(error)

    def create_table(self):
        """Creating postgres table based on .xlsx table

        """
        logger.info("Creating table....")
        if not self.conn:
            self.connect()
        try:
            self.cur.execute(COMMANDS["drop"])
            self.cur.execute(COMMANDS["create"])
            self.conn.commit()
            logger.info("Success!")
        except psycopg2.DatabaseError as error:
            logger.info(error)
            self.connect()

    def show_table(self):
        """Debug function - prints db content

        """
        if not self.conn:
            self.connect()
        try:
            self.cur.execute(COMMANDS["show"])
            column_names = [desc[0] for desc in self.cur.description]
            for i in column_names:
                print("|" + i + "|", end="")
            print("\n"+"--"*90)
            for i in self.cur.fetchall():
                print(i)
                print("--" * 90)

            self.conn.commit()
        except psycopg2.DatabaseError as error:
            logger.info(error)
            self.connect()

    def fill_table(self):
        """Put data from .xlsx to db

        """
        logger.info("Inserting data to DB....")
        if not self.conn:
            self.connect()
        try:
            table = self.read_xlsx()
            self.cur.executemany(COMMANDS["insert"], table)
            self.conn.commit()
            logger.info("Success!")
        except psycopg2.DatabaseError as error:
            logger.info(error)
            self.connect()
