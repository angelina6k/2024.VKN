def calculate_prism_volume():
    a = float(input("Введіть довжину першого катета (a): "))
    b = float(input("Введіть довжину другого катета (b): "))
    h = float(input("Введіть висоту призми (h): "))
        
    base_area = (a * b) / 2
    volume = base_area * h


    print(f"Об'єм призми: {volume:.2f} кубічних одиниць")


calculate_prism_volume()