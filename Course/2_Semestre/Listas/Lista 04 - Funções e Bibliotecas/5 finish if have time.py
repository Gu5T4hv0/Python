def adicionar_a_agenda(agenda):
    add = input("Add someone to the list like 'Ana Paula: 11-9999-1234': ")
    name, number = add.split(":")
    name = name.strip()
    number = number.strip()
    agenda[name] = number
    return agenda

agenda = {
    'Ana Paula': '11-9999-1234',
    'Bruno Silva': '11-8888-5678',
    'Carla Mendes': '11-7777-4321'
    }

print(agenda)

def remover_da_agenda(agenda):
    remove = input("Give me the name of someone you want to remove from the list: ").lower()
    for name, number in agenda.items():
        if remove in name.lower():
                del agenda[remove]
    
    for name, number in agenda.items():
        print(f"{name}: {number}")

agenda = adicionar_a_agenda(agenda)

remover_da_agenda(agenda)