# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44  # информационный объем дискеты в Мб
pages = 100
stroki = 50
chislo_simvolov = 24
for_one_simvol = 4  # 4 байта для хранения одного символа

volume_of_disketa_in_b = volume*1024*1024  # перевод объема дискеты в байты
volume_of_one_book = for_one_simvol*chislo_simvolov*stroki*pages
count_of_books = volume_of_disketa_in_b//volume_of_one_book
print(f"Количество книг, помещающихся на дискету: {count_of_books:.0f}")
