COMMANDS = {
            "drop": """DROP TABLE IF EXISTS data;""",
            "create": """
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
            "show": """SELECT * FROM data""",
            "insert": """INSERT INTO data(
          number, series, issue_date, ending_date, subject, communication_type, organization, place, 
          latitude, longitude, category, usage, RES_name, MAC, call_sign, network_id, azimuth, KA_name, 
          KA_place, power, rec_freq, trans_freq, formula, class, status) VALUES (
          %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        }