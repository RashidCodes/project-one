{% set config = {
    "extract_type": "full"
} %}

select 
    id, 
    name,
    symbol, 
    ingestion_date
from 
    {{ source_table }}