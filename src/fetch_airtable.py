import os
from dotenv import load_dotenv
from airtable import Airtable

def get_data(table):
    load_dotenv() 

    AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
    AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")

    airtable = Airtable(AIRTABLE_BASE_ID, table, api_key=AIRTABLE_API_KEY)
    all_data = airtable.get_all()

    return(all_data)

