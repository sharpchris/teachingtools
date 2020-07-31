import json
from jinja2 import Environment, FileSystemLoader, select_autoescape, Template
from src.fetch_airtable import get_data
from src.build_page import create_page

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


#print(json.dumps(all_tools[0], sort_keys=True, indent=4))

# tool = all_tools[0]['fields']['Tool Name']
# template = Template('The first tool is {{ tool_name }}')
# page_content = template.render(tool_name=tool)



# Templating
jinja = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

# Pass info to index.html tmeplate
template = jinja.get_template('index.html')
page_content = template.render(tool_list=all_tools, category_list=all_categories, pricing_list=all_pricing)

# Write the page content to a file
create_page(page_content)

