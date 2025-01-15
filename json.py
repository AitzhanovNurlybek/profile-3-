import json
print("Interface status")
print("===============================================================")
print("DN                               Description           Speed    MTU  ")
print("--------------------------------- -------------------  ------  ------")
with open("\Users\Aitzh\OneDrive\Рабочий стол\lab4\sample-data.json","r") as file:
    data = json.load(file)
    for item in data["imdata"]:
        print(f"{item['l1PhysIf']['attributes']['dn']}      {item['l1PhysIf']['attributes']['speed']}    {item['l1PhysIf']['attributes']['mtu']}")