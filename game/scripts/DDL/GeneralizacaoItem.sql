CREATE OR REPLACE FUNCTION check_armamento() RETURNS trigger AS -- Procedure para checar se o item adicionado ja pertence a armamento
    $check_armamento$
        BEGIN 
            PERFORM * FROM Armamento WHERE item = NEW.item;
            IF FOUND THEN
                RAISE EXCEPTION 'O Id ja pertence a armamento';
            END IF;
            RETURN NEW;
        END
    $check_armamento$ LANGUAGE plpgsql;

CREATE TRIGGER check_armamento_armadura -- Trigger para adicionar armadura
BEFORE UPDATE OR INSERT ON armadura
FOR EACH ROW
EXECUTE PROCEDURE check_armamento();

CREATE TRIGGER check_armamento_consumivel -- Trigger para adicionar consumivel
BEFORE UPDATE OR INSERT ON consumivel
FOR EACH ROW
EXECUTE PROCEDURE check_armamento();
