from itertools import count

from lxml import html, etree
import os
import json

## get html content using url

# def read_html_content(url):
#     headers = {
#         "User-Agent": "Mozilla/5.0"
#     }
#     response = requests.get(url, headers=headers)
#     tree = html.fromstring(response.text)

#     # convert to formatted HTML
#     formatted_html = etree.tostring(tree, pretty_print=True, encoding="unicode")
#     with open("wendys_html_content.html", "w", encoding="utf-8") as f:
#         f.write(formatted_html)
#     return formatted_html


## get html content using direct file

def read_html_content(file_name):
    current_working_dir = os.getcwd()
    file_path = f"{current_working_dir}/{file_name}"
    with open(file_path, "r", encoding='utf-8') as f :
        html_content = f.read()
    return html_content

def extract_data_from_html(html_content):
    bata_data_dict = {}
    tree = html.fromstring(html_content)
    
    size_path = ".//div[@class='cc-plp--filterDropdown--items cc-plp--filterDropdown--size']//a/@data-refinement-value"
    bata_data_dict["size_data"] = tree.xpath(size_path)
    
    discount_path = ".//div[@class='cc-plp--filterDropdown--items cc-plp--filterDropdown--discountPercent']//a/@aria-label"
    discount_data = tree.xpath(discount_path)
    bata_data_dict["discount_data"] = [discount.replace("Discount: ", "") for discount in discount_data]
    
    brand_path = ".//div[@class='cc-plp--filterDropdown--items cc-plp--filterDropdown--brand']//a/@data-refinement-value"
    bata_data_dict["brand_data"] =tree.xpath(brand_path)

    print("base data dict : ", bata_data_dict)
    
    base_url = "https://www.bata.com/in/men/shoes/slippers-e-flipflop/{brand}/{size}/?prefn1=discountPercent&prefv1={discount}"
    
    bata_url = []
    for brand in bata_data_dict["brand_data"]:
        brand = brand.lower().replace(" ", "-")
        
        for size in bata_data_dict["size_data"]:

            for discount in bata_data_dict["discount_data"]:

                encoded_discount = discount.replace("%", "%25").replace(" ", "%20")
                final_url = base_url.format(
                    brand=brand,
                    size=size,
                    discount=encoded_discount
                )
                bata_url.append(final_url)
    print("\nbase url : ", bata_url)
    print(len(bata_url))

