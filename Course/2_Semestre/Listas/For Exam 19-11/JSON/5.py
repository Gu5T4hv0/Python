import json

user_preferences = {
    "last_login": "2025-11-19",
    "theme": "dark",
    "user_id": 9001,
    "email_notifications": True,
    "language": "en-US"
}

json_string = json.dumps(user_preferences, sort_keys=True, indent=2)

print(json_string)