{% set config = {
    "extract_type": "full"
} %}

{# this query is useless #}
select 
    id, 
    name,
    symbol, 
    ingestion_date
from 
    {{ source_table }}