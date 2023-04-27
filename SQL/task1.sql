-- Создание функции выбора случайных дат проверок
CREATE OR REPLACE FUNCTION get_random_check(min_num_days int, max_num_days int)
	returns SETOF date
	language plpgsql

as
$$
declare
   next_check date := NOW();
   random_dilay int;
begin
   FOR i IN 1..100 LOOP
   		RETURN NEXT next_check;
        random_dilay := (RANDOM() * (max_num_days - min_num_days) + min_num_days)::integer;
   		next_check := next_check + make_interval(days => random_dilay);
   END LOOP;
end;
$$;

-- Создание оператора выбора случайных дат проверок
CREATE OPERATOR <~> (
	FUNCTION = get_random_check,
	LEFTARG = int,  -- Минимальная задержно между проверками (в днях)
	RIGHTARG = int  -- Максимальная задержно между проверками (в днях)
);

SELECT 2 <~> 7;