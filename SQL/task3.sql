CREATE OR REPLACE FUNCTION calculate_remains()
	RETURNS table(acc int, dt_from date, dt_to date, balance int)
as
$$
declare
	i int;
	dates date[];
	amount int;
begin
	FOR acc IN select transfers.from from transfers group by transfers.from order by transfers.from LOOP  -- Цикл по аккаунтам
		balance = 0;
		i = 1;
		dt_to = NULL;
		dates = (select array_agg(transfers.tdate) from transfers where transfers.from = acc or transfers.to = acc);  -- Даты перевода и отправки денег
		FOR dt_from, amount IN select transfers.tdate, CASE WHEN transfers.from = acc THEN -transfers.amount
							 							  WHEN transfers.to = acc THEN transfers.amount END
							 from transfers WHERE transfers.from = acc or transfers.to = acc LOOP  -- Приход\Уход денег, если Приход, то перед amount ставится минус
			balance := balance + amount;
			i = i + 1;
			IF array_length(dates, 1) >= i THEN  -- Если в массиве есть еще дата, то записываем ее
				dt_to = dates[i];
			ELSE
				dt_to = '01.01.3000';  -- Если нет, то ставим 1 января 3000 года
			END IF;	
			RETURN NEXT ;
		END LOOP;
   	END LOOP;
end;
$$ language plpgsql;


select * from calculate_remains();
