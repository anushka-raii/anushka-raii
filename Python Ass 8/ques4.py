#Inventory Manager
inventory = {
    "pen": 120,
    "notebook": 75,
    "eraser": 60,
    "marker": 30
}

inventory["stapler"] = 15
inventory["pen"] = 140
inventory.pop("eraser")

print("Updated Inventory:", inventory)
