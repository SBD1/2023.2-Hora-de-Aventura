CREATE OR REPLACE FUNCTION checar_instancia_morta() RETURNS TRIGGER AS $checar_instancia_morta$
BEGIN
	IF NEW.vida <= 0 THEN
		DELETE FROM instancia WHERE personagem = NEW.personagem AND numero = NEW.numero;
	END IF;
	
	RETURN NEW;
END
$checar_instancia_morta$ LANGUAGE plpgsql;

CREATE TRIGGER checar_instancia_morta
AFTER INSERT OR UPDATE ON instancia
FOR EACH ROW EXECUTE FUNCTION checar_instancia_morta();