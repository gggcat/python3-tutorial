import streamlit as st
from dynamodb_connection import DynamoDBConnection, DynamoDBTableEditor

# Create a connection:
conn = st.connection(
    "my_dynamodb_connection", type=DynamoDBConnection, api_type="pandas"
)

# Launch the table editor:
table_editor = DynamoDBTableEditor(conn)
table_editor.edit()

#
# Multiple indexに対応してない。。。。
#