import openpyxl
import psycopg2


class DBHandler:
    def __init__(self):
        self.conn = None
        self.commands = {
            """CREATE TABLE data (
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
                    )""": "create"
        }

    def read_xlsx(self):
        dataframe = openpyxl.load_workbook("data.xlsx")
        dataframe1 = dataframe.active

        for row in range(1, dataframe1.max_row):
            for col in dataframe1.iter_cols(1, dataframe1.max_column):
                print(col[row].value)
                pass

    def connect(self):
        try:
            self.conn = psycopg2.connect(database="postgres", user="postgres", password="user", host="localhost",
                                         port="5433")
            cur = self.conn.cursor()
            for command in self.commands:
                cur.execute(command)
            cur.close()
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()


if __name__ == "__main__":
    db = DBHandler()
    db.connect()

