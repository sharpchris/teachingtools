import json, logging
from jinja2 import Environment, FileSystemLoader, select_autoescape, Template
from src.fetch_airtable import get_data
from src.build_page import create_page
import azure.functions as func
import os
from dotenv import load_dotenv

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    load_dotenv()

    # Fetch data from Airtable. Function requires a str that is the name of the table
    all_tools = get_data('Tools')
    all_categories = get_data('Categories')

    # Define the dictionary of possible pricing structures according to how it is worded in Airtable
    all_pricing = {
        "Free or Free Tier Available": "free",
        "Paid for by Faculty / Department": "facultyPays",
        "Paid for by Students": "studentPays",
        "Paid for by Both / Either": "eitherPay"
    }

    print(json.dumps(all_tools, sort_keys=True, indent=4))

    ## Templating
    # Set template folder location
    template_path=os.getenv("TEMPLATE_PATH")

    # Create Jinja2 environment
    jinja = Environment(
        loader=FileSystemLoader(template_path),
        autoescape=select_autoescape(['html'])
    )

    # Pass info to template.html
    template = jinja.get_template('template.html')
    page_content = template.render(tool_list=all_tools, category_list=all_categories, pricing_list=all_pricing)

    # Write the page content to a file
    create_page(page_content)

    # Example Content for HTTP Azure Function
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        print(name)
        return func.HttpResponse(f"Hello {name}!")
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )

# If the file is directly executed, call the main function
if __name__ == '__main__':
    request = func.HttpRequest(
        "GET",
        "localhost",
        params = {"name": "Chris"},
        body = b'Hello World'
    )
    main(request)