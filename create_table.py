def phones_create():
    import sqlite3

    con = sqlite3.connect('phones.db')
    cur = con.cursor()
    sql = """
        CREATE TABLE Phones (
            phoneID INTEGER PRIMARY KEY,
            contactName VARCHAR(100),
            phoneValue VARCHAR(20)
        );
        """
    cur.execute(sql)
    con.commit()
    con.close()