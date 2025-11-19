import json

orders_json = '''
{
    "company": "Acme Widgets Inc.",
    "orders": [
        {
            "order_id": "A1001",
            "customer": "Alice",
            "items": [
                {"product": "Widget X", "quantity": 5},
                {"product": "Gizmo Y", "quantity": 2}
            ]
        },
        {
            "order_id": "A1002",
            "customer": "Bob",
            "items": [
                {"product": "Gadget Z", "quantity": 10},
                {"product": "Widget X", "quantity": 1}
            ]
        }
    ]
}
'''

data = json.loads(orders_json)

order_list = data['orders']
total_items = 0
for i in order_list:
    items = i['items']
    for j in items:
        value = j['quantity']
        total_items += value

print(total_items)