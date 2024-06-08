from google.cloud.bigquery import SchemaField

TABLE_SCHEMA = [
    SchemaField("url", "STRING"),
    SchemaField("title", "STRING"),
    SchemaField("authors", "STRING", mode="REPEATED"),
    SchemaField("hat", "STRING"),
    SchemaField("tags", "STRING", mode="REPEATED"),
    SchemaField("text", "STRING"),
]
