drop table if exists {{ target_table }};

create table {{ target_table }} as
	select 
		"Date",
		round("Price", 2) as Price,
		id,
		ingestion_date,
		id_date
	from public.coin_price_history;