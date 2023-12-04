-- FUNCTION: public.checar_instancia_morta()

-- DROP FUNCTION IF EXISTS public.checar_instancia_morta();

CREATE OR REPLACE FUNCTION public.checar_instancia_morta()
    RETURNS trigger
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE NOT LEAKPROOF
AS $BODY$
BEGIN
	IF NEW.vida <= 0 THEN
		DELETE FROM instancia WHERE personagem = NEW.personagem AND numero = NEW.numero;
	END IF;
	
	RETURN NEW;
END
$BODY$;

ALTER FUNCTION public.checar_instancia_morta()
    OWNER TO postgres;
