from datetime import datetime, timedelta
def datas_e_prazos(data_str, prazo):
    data = datetime.strptime(data_str, "%Y-%m-%d").date()
    count = 0
    current_day = data

    while count < prazo:
        current_day += timedelta(days=1)
        if current_day.weekday() < 5:
            count += 1
        
    print(f"¨The deadline from now: {current_day}")

datas_e_prazos('2025-03-13' , 5)