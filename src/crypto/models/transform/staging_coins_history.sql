drop table if exists {{ target_table }};

create table {{ target_table }} as
	select 
		id_date,
		id as coin_name,
		price_date as price_extraction_date,
		current_price,
		market_cap,
		ingestion_date 
	from public.coins_history;