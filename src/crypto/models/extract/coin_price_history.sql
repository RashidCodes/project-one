{% set config = {
    "extract_type": "incremental", 
    "incremental_column": "ingestion_date",
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
    where ingestion_date > '{{ incremental_value }}'
{% endif %}