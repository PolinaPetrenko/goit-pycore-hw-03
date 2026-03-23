import random

def get_numbers_ticket(min_val, max_val, quantity):
    if not (1 <= min_val <= quantity <= max_val <= 1000):
        return []
    numbers = random.sample(range(min_val, max_val + 1), quantity)
    return sorted(numbers)


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)