import openpyxl
import psycopg2


class DBHandler:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.commands = {
            "create":"""DROP TABLE IF EXISTS data; 
               CREATE TABLE data (
                    number INTEGER PRIMARY KEY,
                    series VARCHAR(5) NOT NULL,
                    issue_date DATE NOT NULL,
                    ending_date DATE NOT NULL,
                    subject VARCHAR(50) NOT NULL,
                    communication_type VARCHAR(50) NOT NULL,
                    organization VARCHAR(50) NOT NULL,
                    place VARCHAR(200) NOT NULL,
                    category INTEGER,
                    usage INTEGER,
                    RES_name VARCHAR(50) NOT NULL,
                    MAC VARCHAR(50),
                    call_sign VARCHAR(50),
                    network_id VARCHAR(50),
                    azimuth VARCHAR(50),
                    KA_name VARCHAR(50),
                    KA_place VARCHAR(50),
                    power VARCHAR(50),
                    rec_freq VARCHAR(100),
                    trans_freq VARCHAR(100),
                    formula VARCHAR(50),
                    class VARCHAR(50),
                    status VARCHAR(50)
                    );""",
            "show": """SELECT * FROM data"""
        }

        self.connect()


    def read_xlsx(self):
        dataframe = openpyxl.load_workbook("data.xlsx")
        dataframe1 = dataframe.active

        for row in range(1, dataframe1.max_row):
            for col in dataframe1.iter_cols(1, dataframe1.max_column):
                print(col[row].value)
                pass

    def connect(self):
        try:
            self.conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="127.0.0.1",
                                         port="5433")
            self.cur = self.conn.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def create_table(self):
        if not self.conn:
            self.connect()
        try:
            self.cur.execute(self.commands["create"])
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.connect()

    def show_table(self):
        if not self.conn:
            self.connect()
        try:
            self.cur.execute(self.commands["show"])
            column_names = [desc[0] for desc in self.cur.description]
            for i in column_names:
                print("|" + i + "|", end="")
            print("\n"+"--"*90)
            for i in self.cur.fetchall():
                print(i)

            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.connect()


if __name__ == "__main__":
    db = DBHandler()
    db.create_table()
    db.show_table()


