import psycopg2, psycopg2.extras, os

host = os.environ["DBHOST"]
database = os.environ["DATABASE"]
user = os.environ["DBUSER"]
password = os.environ["DBPASSWORD"]
table = os.environ["TABLE"]


def lookupSymbol(symbol):
    conn = psycopg2.connect(host=host, database=database, user=user, password=password)
    stmt = f"""SELECT cp,op,bv,bu,sb,yd,om,dv,pe,symbol,to_char(created_at,'DD Mon YYYY HH12:MI:SS ') as date,
    extract(day from AGE(NOW(),created_at))||' Days '||
    extract(hour from AGE(NOW(),created_at))||' Hours '||
    extract(minute from AGE(NOW(),created_at))||' Minutes' as age,
    company_name, company_desc FROM {table} WHERE symbol = '{symbol}' ORDER BY created_at DESC"""
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(stmt)
    result = cur.fetchall()
    cur.close()
    conn.close()
    if len(result) >= 1:
        return result
    else:
        return False


def storeResult(cp, op, bv, bu, sb, yd, om, dv, pe, symbol, name, desc):
    conn = psycopg2.connect(host=host, database=database, user=user, password=password)
    stmt = f"INSERT INTO {table}(cp,op,bv,bu,sb,yd,om,dv,pe,symbol,company_name,company_desc) VALUES ({cp},{op},{bv},{bu},{sb},{yd},{om},{dv},{pe},'{symbol}',{name},{desc})"
    cur = conn.cursor()
    cur.execute(stmt)
    cur.close()
    conn.commit()
    conn.close()
    return None
