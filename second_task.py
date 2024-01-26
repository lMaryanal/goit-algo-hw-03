import random

def get_numbers_ticket(min, max, quantity)-> list: #повертатє випадковий набір чисел у межах заданих параметрів
    if (max - min) >= quantity and min >= 1 and max <= 1000: #обмеження
        random_numbers = random.sample(range(min, max+1), quantity) #вибір випадкових унікальних чисел
        random_numbers.sort()
        return (random_numbers)
    else:
        return([])


def get_numbers_ticket2(min, max, quantity): #повертатє випадковий набір чисел у межах заданих параметрів
    if (max - min) >= quantity and min >= 1 and max <= 1000: #обмеження
        random_numbers = set()
        while len(random_numbers) < quantity:           #додає випадкове число у множину поки вона не стане потрібної довжини
            random_numbers.add(random.randint(min, max))
        return (list(random_numbers))
    else:
        return([])
    
print(get_numbers_ticket(22, 30, 6))

