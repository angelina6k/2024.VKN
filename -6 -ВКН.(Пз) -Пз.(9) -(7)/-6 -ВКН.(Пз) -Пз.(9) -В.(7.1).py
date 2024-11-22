def generate_polygon_name(sides, start_letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    start_index = alphabet.index(start_letter.upper())
    polygon_name = ""
    
    for i in range(sides):
        letter_index = (start_index + i) % len(alphabet)
        polygon_name += alphabet[letter_index]
    
    return polygon_name


sides = int(input("Введіть кількість кутів многокутника: "))
start_letter = input("Введіть першу літеру назви: ").strip()

result = generate_polygon_name(sides, start_letter)
print("Назва многокутника:", result)