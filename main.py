from flask import Flask, request

app = Flask(__name__)


@app.route('/phones/create/')
def phones_create():
    phoneID = request.args.get('phoneID')
    contactName = request.args.get('contactName')
    phoneValue = request.args.get('phoneValue')
    import sqlite3

    con = sqlite3.connect('phones.db')
    cur = con.cursor()

    sql = """
    INSERT INTO Phones (phoneID, contactName, phoneValue)
    VALUES (?, ?, ?)
    """
    cur.execute(sql, (phoneID, contactName, phoneValue))
    con.commit()
    con.close()
    return f'{contactName}, {phoneValue} created'


@app.route('/phones/update/')
def phones_update():
    phoneID = request.args.get('phoneID')
    contactName = request.args.get('contactName')
    phoneValue = request.args.get('phoneValue')

    import sqlite3
    con = sqlite3.connect('phones.db')
    cur = con.cursor()

    sql = """
    UPDATE Phones 
    SET contactName = ?, phoneValue = ?
    WHERE phoneID = ?
    """
    cur.execute(sql, (contactName, phoneValue, phoneID))
    con.commit()
    con.close()
    return f'{contactName}, {phoneValue} updated'


@app.route('/phones/delete/')
def phones_delete():
    phoneID = request.args.get('phoneID')

    import sqlite3
    con = sqlite3.connect('phones.db')
    cur = con.cursor()

    sql = """
    DELETE FROM Phones 

    WHERE phoneID = ?
    """
    cur.execute(sql, phoneID)
    con.commit()
    con.close()

    return f'Table {phoneID} deleted'


@app.route('/phones/read/')
def phones_read():
    import sqlite3
    con = sqlite3.connect('phones.db')
    cur = con.cursor()
    sql = """
    SELECT * FROM Phones
    ORDER BY contactName;
          """
    cur.execute(sql)
    phones = cur.fetchall()
    con.close()
    return str(phones)


if __name__ == '__main__':
    app.run()
