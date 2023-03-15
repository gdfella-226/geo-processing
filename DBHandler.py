import openpyxl
import psycopg2


class DBHandler:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.commands = {
            "create":"""DROP TABLE IF EXISTS data; 
               CREATE TABLE data (
                    number VARCHAR(100),
                    series VARCHAR(100),
                    issue_date VARCHAR(100),
                    ending_date VARCHAR(100),
                    subject VARCHAR(100),
                    communication_type VARCHAR(100),
                    organization VARCHAR(100),
                    place VARCHAR(255),
                    latitude VARCHAR(100),
                    longitude VARCHAR(100),
                    category VARCHAR(100),
                    usage VARCHAR(100),
                    RES_name VARCHAR(100),
                    MAC VARCHAR(100),
                    call_sign VARCHAR(100),
                    network_id VARCHAR(100),
                    azimuth VARCHAR(100),
                    KA_name VARCHAR(100),
                    KA_place VARCHAR(100),
                    power VARCHAR(100),
                    rec_freq VARCHAR(255),
                    trans_freq VARCHAR(255),
                    formula VARCHAR(100),
                    class VARCHAR(100),
                    status VARCHAR(100)
                    );""",
            "show": """SELECT * FROM data"""
        }

        self.connect()

    @staticmethod
    def read_xlsx():
        dataframe = openpyxl.load_workbook("data.xlsx")
        dataframe1 = dataframe.active
        table = [[] for i in range(dataframe1.max_row)]
        for row in range(1, dataframe1.max_row):
            for col in dataframe1.iter_cols(1, dataframe1.max_column):
                table[row].append(col[row].value)
        return table

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

    def fill_table(self):
        if not self.conn:
            self.connect()
        try:
            column_names = [desc[0] for desc in self.cur.description]
            command = "INSERT INTO data("
            c = 0
            for i in column_names:
                command += (i + ", ")
                c += 1
            command = command[:-2] + ") VALUES(%(val)s)"
            frame = openpyxl.load_workbook("data.xlsx").active

            for row in range(1, frame.max_row):
                tmp = []
                for col in frame.iter_cols(0, frame.max_column):
                    if not col[row].value:
                        tmp.append('')
                    else:
                        tmp.append(col[row].value)
                if len(tmp) == 25:
                    value = str(tmp).replace('[', '(').replace(']', ')')
                    print(value)
                    print(f"({c}, {len(tmp)})")
                    self.cur.execute(command, {"val": value})

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.connect()




if __name__ == "__main__":
    db = DBHandler()
    db.create_table()
    db.show_table()
    #print(db.read_xlsx())
    db.fill_table()


