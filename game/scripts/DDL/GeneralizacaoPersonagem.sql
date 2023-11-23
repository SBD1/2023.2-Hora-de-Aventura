CREATE OR REPLACE FUNCTION check_pc() RETURNS trigger AS -- Procedure para checar se o item adicionado ja pertence a pc
    $check_pc$
        BEGIN 
            PERFORM * FROM pc WHERE Personagem = NEW.Personagem;
            IF FOUND THEN
                RAISE EXCEPTION 'O Id ja pertence a pc';
            END IF;
            RETURN NEW;
        END
    $check_pc$ LANGUAGE plpgsql;

CREATE TRIGGER check_pc -- Trigger para adicionar NPC
BEFORE UPDATE OR INSERT ON npc
FOR EACH ROW
EXECUTE PROCEDURE check_pc();