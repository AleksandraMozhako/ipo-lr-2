n = int(input("Введите количество школьников: "))
k = int(input("Введите количество яблок: "))
appl_per_child = k // n
apple_in_bask = k % n
print("Количество яблок на каждого школьника: ", appl_per_child, "Количество яблок в корзине: ", apple_in_bask  )