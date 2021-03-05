import psycopg2, psycopg2.extras, os, string, random

# host = os.environ['DBHOST']
# database = os.environ['DATABASE']
# user = os.environ['DBUSER']
# password = os.environ['DBPASSWORD']
host = "ziggy.db.elephantsql.com"
database = "vzcelume"
user = "vzcelume"
password = "epA6XSX4ik41NJrEwzbtBj2KvbWFML51"


def lookupSymbol(symbol):
    conn = psycopg2.connect(host=host, database=database, user=user, password=password)
    stmt = f"SELECT cp,op,bv,bu,sb,yd,om,dv,pe,symbol,to_char(created_at,'DD Mon YYYY HH12:MI:SS '), age(NOW(),created_at) as age FROM stock_history WHERE symbol = '{symbol}' ORDER BY created_at DESC"
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(stmt)
    result = cur.fetchall()
    cur.close()
    conn.close()
    if len(result) >= 1:
        return result
    else:
        return False


def storeResult(cp, op, bv, bu, sb, yd, om, dv, pe, symbol):
    conn = psycopg2.connect(host=host, database=database, user=user, password=password)
    stmt = f"INSERT INTO stock_history(cp,op,bv,bu,sb,yd,om,dv,pe,symbol) VALUES ({cp},{op},{bv},{bu},{sb},{yd},{om},{dv},{pe},'{symbol}')"
    cur = conn.cursor()
    cur.execute(stmt)
    cur.close()
    conn.commit()
    conn.close()
    return None
