# from urllib.parse import quote

# discount_list = [
#     'up to 10%',
#     'from 11 to 20%',
#     'from 21 to 30%',
#     'from 31 to 40%',
#     'All Discounted'
# ]

# base_url = "https://www.bata.com/in/men/shoes/slippers-e-flipflop/{brand}/{size}/?prefn1=discountPercent&prefv1={discount}"

# brand = "bata"
# size = "8"

# for discount in discount_list:
#     encoded_discount = quote(discount)
#     final_url = base_url.format(
#         brand=brand,
#         size=size,
#         discount=encoded_discount
#     )
#     print(final_url)





discount_list = [
    'up to 10%',
    'from 11 to 20%',
    'from 21 to 30%',
    'from 31 to 40%',
    'All Discounted'
]

base_url = "https://www.bata.com/in/men/shoes/slippers-e-flipflop/{brand}/{size}/?prefn1=discountPercent&prefv1={discount}"

brand = "bata"
size = "8"

for discount in discount_list:
    encoded_discount = discount.replace("%", "%25").replace(" ", "%20")
    print(encoded_discount)
    
    final_url = base_url.format(
        brand=brand,
        size=size,
        discount=encoded_discount
    )
    
    print(final_url)
    break