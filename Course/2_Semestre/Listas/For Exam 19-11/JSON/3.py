import json

server_status = {
    "server_id": "WEB-001",
    "status": "online",
    "load_average": [0.5, 0.45, 0.42],
    "services": {
        "api": {"port": 8080, "health": "ok"},
        "database": {"port": 3306, "health": "degraded"}
    },
    "timestamp": 1732044666
}

with open('status_report.json', 'w') as file:
    json.dump(server_status, file, indent=4)