from main import *
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from io import BytesIO
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

functions = [league_table,top_scorers,detail_top,player_table,all_time_table,all_time_winner_club,top_scorers_seasons,goals_per_season]

def to_blob(func):
    file_name = func.__name__
    func = func()


    # Convert DataFrame to Arrow Table
    table = pa.Table.from_pandas(func)

    parquet_buffer = BytesIO()
    pq.write_table(table, parquet_buffer)

    connection_string = ""
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    container_name = "testtech"
    blob_name = f"{file_name}.parquet"
    container_client = blob_service_client.get_container_client(container_name)

    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(parquet_buffer.getvalue(), overwrite=True)
    print(f"{blob_name} successfully updated")


for items in functions:
    to_blob(items)