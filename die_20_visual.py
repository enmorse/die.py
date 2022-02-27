from main import Die

die = Die()

results = []

for roll_num in range(1):
    result = die.roll_die_20()
    results.append(result)

print(results)
