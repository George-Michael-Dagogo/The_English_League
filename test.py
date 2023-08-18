from main import *
import pandas as pd
def to_blob(func):
    file_name = func.__name__
    func = func()
    blob_name = f"{file_name}.parquet"
    print(blob_name)

to_blob(detail_top)