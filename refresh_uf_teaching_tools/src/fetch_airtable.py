import os
from dotenv import load_dotenv
from airtable import Airtable

def get_data(table):
    load_dotenv() 

    AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
    AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")

    airtable = Airtable(AIRTABLE_BASE_ID, table, api_key=AIRTABLE_API_KEY)

    # Only published Tools should be returned; for other tables return all
    if table == "Tools":
        all_data = airtable.search('Publish', 1)
    else:
        all_data = airtable.get_all()

    return(all_data)

