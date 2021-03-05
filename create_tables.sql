CREATE TABLE stock_history(
    id SERIAL PRIMARY KEY,
    cp INT,
    op INT,
    bv INT,
    bu INT,
    sb INT,
    yd INT,
    om INT,
    dv INT,
    pe INT,
    symbol VARCHAR,
    company_name VARCHAR,
    company_desc VARCHAR,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE test(
    id SERIAL PRIMARY KEY,
    cp INT,
    op INT,
    bv INT,
    bu INT,
    sb INT,
    yd INT,
    om INT,
    dv INT,
    pe INT,
    symbol VARCHAR,
    company_name VARCHAR,
    company_desc VARCHAR,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- SELECT
--   'DROP TABLE IF EXISTS "' || tablename || '" CASCADE;' 
-- from
--   pg_tables WHERE schemaname = 'public';