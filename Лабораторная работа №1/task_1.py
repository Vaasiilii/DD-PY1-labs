numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
delete_number = numbers[4]
new_numbers = [2, -93, -2, 8, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
average_instaed_of_missing = sum(new_numbers)/(len(new_numbers)+1)
numbers[4] = average_instaed_of_missing
print("Измененный список:", numbers)
