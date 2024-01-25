import re


def normalize_phone(phone_number): #нормалізує телефонні номери до стандартного формату +38xxxxxxxxxx
    pattern = r"[\d\+]+" #шаблон вибору з рядка всіх чисел >=1 та +
    normalised_number = re.findall(pattern, phone_number) #вибирає з рядка всі значення за шаблоном та формує з них список
    normalised_number = ''.join(normalised_number) 
    if not normalised_number.startswith("+"): # перевіряє чи номер повний, якщо ні, то додає необхідне
        normalised_number = "+38"+ normalised_number if len(normalised_number) == 10 else "+"+ normalised_number
    return(normalised_number)


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
