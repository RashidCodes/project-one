{% set config = {
    "extract_type": "incremental", 
    "incremental_column": "date",
    "key_columns":["id_date"]
} %}

select 
    id_date,
    id, 
    date, 
    current_price, 
    market_cap, 
    ingestion_date
from 
    {{ source_table }}

{% if is_incremental %}
    where date > '{{ incremental_value }}'
{% endif %}