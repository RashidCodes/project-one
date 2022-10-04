drop table if exists {{ target_table }}; 

create table {{ target_table }} as (
    select id,
           name,
           symbol,
           To_Date(ingestion_date,'dd-mm-YYYY') as ingestion_date
    from coins
);