import os
from algoliasearch.search_client import SearchClient

client = SearchClient.create(os.environ['ALGOLIA_APP_ID'], os.environ['ALGOLIA_API_KEY'])
index = client.init_index(os.environ['ALGOLIA_INDEX_NAME'])

res = index.search('python')
for item in res['hits']:
    print(item['title'])
