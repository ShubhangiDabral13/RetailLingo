from langchain.llms import GooglePalm
api_key = 'AIzaSyAY41ZD0NEBOxgcwT37qysUSkYJaD0DgWs '
llm = GooglePalm(google_api_key=api_key, temperature=0.2)

#importing the sql connection database
from langchain.utilities import SQLDatabase
#creating chain to connect to the sql database model
from langchain_experimental.sql import SQLDatabaseChain

db_user = "root"
db_password = "shubhangi"
db_host = "localhost"
db_name = "atliq_tshirts"

db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",sample_rows_in_table_info=3)

# print(db.table_info)


db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
print("hello")
qns1 = db_chain("How many t-shirts do we have for Nike in small size and white color?")

# qns1 = db_chain("How much is the price of the inventory for all small size t-shirts?")