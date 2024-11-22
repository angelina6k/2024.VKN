# Ініціалізація словника з площами 5 областей
areas = {
    'Київська': 28300,
    'Львівська': 21500,
    'Одеська': 33500,
    'Дніпропетровська': 31800,
    'Харківська': 31400
}

def add_area(area_name, area_size):
    areas[area_name] = area_size
    print(f"Область {area_name} з площею {area_size} км² додана.")

def search_area(area_name):
    if area_name in areas:
        print(f"Площа {area_name}: {areas[area_name]} км²")
    else:
        print(f"Область {area_name} не знайдена.")

def delete_area(area_name):
    if area_name in areas:
        del areas[area_name]
        print(f"Область {area_name} видалена.")
    else:
        print(f"Область {area_name} не знайдена.")

add_area('Вінницька', 26000)
search_area('Львівська')
delete_area('Харківська')

print("\nОновлений словник площ:")
for area, size in areas.items():
    print(f"{area}: {size} км²")