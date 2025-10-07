n = int(input("Введите количество школьников: "))
k = int(input("Введите количество яблок: "))
apples_per_child = k // n
apples_in_basket = k % n
print("Количество яблок на каждого школьника:", apples_per_child, "Количество яблок в корзине:", apples_in_basket  )