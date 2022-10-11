{% set config = {
    "extract_type": "full"
} %}

{# this query is useless #}
select 
    id, 
    market_cap_rank,
    score, 
    ingestion_date
from 
    {{ source_table }}