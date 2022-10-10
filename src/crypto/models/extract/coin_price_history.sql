{% set config = {
    "extract_type": "incremental", 
    "incremental_column": "price_datetimestamp",
    "key_columns":["id_date"]
} %}

select 
    id_date,
    id, 
    price_datetimestamp, 
    Price, 
    ingestion_date
from 
    {{ source_table }}

{% if is_incremental %}
    where date > '{{ incremental_value }}'
{% endif %}