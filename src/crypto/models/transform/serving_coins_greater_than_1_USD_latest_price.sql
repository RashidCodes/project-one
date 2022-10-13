drop table if exists {{ target_table }};

create table {{ target_table }} as 
	with s as (
	Select id, max("Date") as latest_date from public.coin_price_history
	group by id
	)
select "Date", "Price", hist."id" as "Coin", "ingestion_date", "id_date", "latest_date" from public.coin_price_history hist
right join s on hist."Date" = s."latest_date"
where hist."Price" > 1
order by hist."Price" desc;
--join, rename, sorting, where