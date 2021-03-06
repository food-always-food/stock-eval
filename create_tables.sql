CREATE TABLE stock_history(
    id SERIAL PRIMARY KEY,
    cp NUMERIC,
    op NUMERIC,
    bv NUMERIC,
    bu NUMERIC,
    sb NUMERIC,
    yd NUMERIC,
    om NUMERIC,
    dv NUMERIC,
    pe NUMERIC,
    symbol VARCHAR,
    company_name VARCHAR,
    company_desc VARCHAR,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE test(
    id SERIAL PRIMARY KEY,
    cp NUMERIC,
    op NUMERIC,
    bv NUMERIC,
    bu NUMERIC,
    sb NUMERIC,
    yd NUMERIC,
    om NUMERIC,
    dv NUMERIC,
    pe NUMERIC,
    symbol VARCHAR,
    company_name VARCHAR,
    company_desc VARCHAR,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- SELECT
--   'DROP TABLE IF EXISTS "' || tablename || '" CASCADE;' 
-- from
--   pg_tables WHERE schemaname = 'public';