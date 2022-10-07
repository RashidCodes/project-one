{% set config = {
    "extract_type": "full"
} %}

select 
    id, 
    market_cap_rank,
    score, 
    ingestion_date
from 
    {{ source_table }}