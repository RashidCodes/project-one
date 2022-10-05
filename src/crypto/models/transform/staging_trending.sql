drop table if exists {{ target_table }}; 

create table {{ target_table }} as (
    select id,
            Cast(market_cap_rank as INT) as market_cap_rank,
            Cast(score as INT) as score,
            To_Date(ingestion_date,'dd-mm-YYYY') as ingestion_date
    from trending
);