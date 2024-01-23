import random

def get_numbers_ticket(min, max, quantity):
    if min <= quantity <= max and min >= 1 and max <= 1000:
        random_numbers = random.sample(range(min, max+1), quantity)
        random_numbers.sort()
        return (random_numbers)
    else:
        return([])


def get_numbers_ticket2(min, max, quantity):
    if min <= quantity <= max and min >= 1 and max <= 1000:
        random_numbers = set()
        while len(random_numbers) < quantity:
            random_numbers.add(random.randint(min, max))
        return (list(random_numbers))
    else:
        return([])
    
print(get_numbers_ticket(1, 22, 10))

