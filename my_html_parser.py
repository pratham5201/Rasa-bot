
import requests
from bs4 import BeautifulSoup


def create_dictionary_from_url(url):
    # Fetch HTML content from the URL
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # Initialize an empty dictionary to store the results
    result_dict = {}

    # Find all the headings
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

    # Iterate through the headings
    for heading in headings:
        # Get the text of the heading
        heading_text = heading.get_text(strip=True)

        # Find the next heading
        next_heading = heading.find_next(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

        # Collect all content until the next heading
        content = []
        
        current_element = heading.find_next(['p', 'ul', 'ol'])
        # print(current_element,"current text")
        while current_element and current_element != next_heading and not current_element.name.startswith('h'):
            current = current_element.get_text(strip=True)
            cleaned_text = current.replace('\xa0', ' ')
            #breakpoint()
            content.append(cleaned_text)

            current_element = current_element.find_next(['p', 'ul', 'ol', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

        # Remove empty strings from the content
        content = [c for c in content if c]


        # Store the content in the dictionary
        result_dict[heading_text] = content

    return result_dict

def main(list_of_routes):
    qna_data = {}
    
    # Example usage with a website URL
    for each in list_of_routes:
        website_url = f'https://help.assetpanda.com/{each}.html'
        ans = create_dictionary_from_url(website_url)
        for key, value in ans.items():
            qna_data[key] = value
    return qna_data




#  ,"Delete_Groups","Edit_Groups","Consumables_and_Inventory_Management","Group_Actions_and_Returns","Group_Scan"


list_of_routes = ["Group_Actions_and_Returns","Edit_Groups","Group_Scan","Consumables_and_Inventory_Management"]
qna_data = main(list_of_routes)


# print(qna_data,"qna_data:1")





