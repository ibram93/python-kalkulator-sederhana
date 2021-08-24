while True:
    print("Kalkulator Sederhana ")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Pembagian")
    print("4. Perkalian")
    
    pil = int(input("Pilih operasi: "))
    while pil > 4 or pil == 0:
        print("Pilihan operasi 1 - 4")
        pil = int(input("Pilih operasi: "))
        
    x_str = str(input("Bilangan 1: "))
    while x_str == "":
        x_str = str(input("Bilangan 1: "))
    x = int(x_str)
    
    y_str = str(input("Bilangan 2: "))
    while y_str == "":
        y_str = str(input("Bilangan 2: "))
    y = int(y_str)
    
    
    if pil == 1:
        opr = "+"
        hasil = x + y
    elif pil == 2:
        opr = "-"
        hasil = x-y
    elif pil == 3:
        opr = ":"
        if y == 0:
            print("pilih angka pembagi selain 0")
            hasil = "error"
        else:
            hasil = x / y
    elif pil == 4:
        opr = "x"
        hasil = x * y
            
    print(f"Hasil dari {x} {opr} {y} adalah {hasil}")
    
    