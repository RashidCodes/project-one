drop table if exists {{ target_table }}; 

create table {{ target_table }} (
    id_date VARCHAR ( 50 ) UNIQUE PRIMARY KEY,
	id VARCHAR ( 50 ) NOT NULL,
	date Date NOT NULL,
	current_price Float,
	market_cap Float,
    ingestion_date VARCHAR ( 255 ) NOT NULL
);

insert into {{ target_table }} (id_date, id, date, current_price, market_cap, ingestion_date)
select id_date
		,id
		,To_Date(price_date ,'DD-MM-YYYY') as price_date
		,current_price ::float
	    ,market_cap ::float
		,To_Date(ingestion_date,'dd-mm-YYYY') as ingestion_date
from coins_history;