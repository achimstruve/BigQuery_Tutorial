# tutorial based on this YT video: https://www.youtube.com/watch?v=lLPdRRy7dfE&list=PL3JVwFmb_BnRKqcbtl2hHL5GIQOHX-sC5&index=1
import os
from google.cloud import bigquery

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'CloudDemo_AS_Service.json'
           
client = bigquery.Client()

sql_query = """
SELECT station_id, name, dockcount
FROM `bigquery-public-data.san_francisco.bikeshare_stations`
LIMIT 50
"""

query_job = client.query(sql_query)

for row in query_job.result():
    print(row)

print(query_job.to_dataframe())
