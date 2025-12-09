import json

product_catalog_json = '''
[
    {
        "category": "Apparel",
        "product_name": "T-Shirt",
        "base_sku": "TS001",
        "variants": [
            {"size": "S", "color": "Red", "sku": "TS001-R-S", "price": 15.99},
            {"size": "M", "color": "Red", "sku": "TS001-R-M", "price": 15.99},
            {"size": "L", "color": "Blue", "sku": "TS001-B-L", "price": 17.99}
        ]
    },
    {
        "category": "Apparel",
        "product_name": "Hoodie",
        "base_sku": "HD002",
        "variants": [
            {"size": "M", "color": "Black", "sku": "HD002-K-M", "price": 39.99}
        ]
    }
]
'''

catalog_data = json.loads(product_catalog_json)

transformed_catalog = []
for i in catalog_data:
    category = i['category']
    product_name = i['product_name']
    variants = i['variants']
    for j in variants:
        new = {}
        new['Category'] = category
        new['Product Name'] = product_name
        new['SKU'] = j['sku']
        new['Price'] = j['price']
        transformed_catalog.append(new)
print(transformed_catalog)