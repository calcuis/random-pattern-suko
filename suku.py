import random

def generate_random_pattern():
    digits = list(range(1, 10))
    random.shuffle(digits)
    pattern = ''.join(map(str, digits))
    return pattern

def calculate_sums(pattern):
    sums = []
    for indices in [(0, 1, 3, 4), (1, 2, 4, 5), (3, 4, 6, 7), (4, 5, 7, 8)]:
        current_sum = sum(int(pattern[i]) for i in indices)
        sums.append(current_sum)
    return sums

def calculate_hints(pattern):
    hints = []
    for indices in [(0, 1, 3), (2, 4, 5, 8), (6, 7)]:
        current_hint = sum(int(pattern[i]) for i in indices)
        hints.append(current_hint)
    return hints

random_pattern = generate_random_pattern()
print("Random Pattern:", random_pattern)

sums = calculate_sums(random_pattern)
print("Sums:", sums)

hints = calculate_hints(random_pattern)
print("Hints:", hints)
