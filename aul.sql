-- create table exer (
--     id integer,
--     nome varchar(50)
-- );

-- CREATE FUNCTION selecionar(p_itemno int)
-- RETURNS setof dados AS $$
-- BEGIN
--     RETURN QUERY SELECT * FROM dados AS s 
--                  WHERE s.id = p_itemno;
-- END;
-- $$ LANGUAGE plpgsql;

-- CREATE FUNCTION sales_tax(subtotal real) RETURNS real AS $$
-- BEGIN
--     RETURN subtotal * 0.06;
-- END;
-- $$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION text_return (varchar dado)
RETURNS dado AS $$
    RETURN dado;
$$ LANGUAGE plpgsql;