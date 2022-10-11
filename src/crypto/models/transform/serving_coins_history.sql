drop table if exists {{ target_table }};

create table {{ target_table }} as 
	select 
		id_date,
		coin_name,
		price_extraction_date,
		round(current_price, 2) as current_price,
		round(market_cap, 2) as market_cap,
		ingestion_date as ingestion_timestamp 
	from public.staging_coins_history;