# Collatz Problem

biggest_sequece = 1
biggest_sequece_num = 1
aleady_found = {1000000}

def find_collatz(num):
    if num % 2 == 0:
        return num/2
    else:
        return 3 * num + 1

for i in range (1, 1000000):
    j = 1000000 - i
    counter = 1
    collatz_num = j
    if j in aleady_found:
        continue
    while collatz_num != 1:
        counter = counter + 1
        collatz_num = find_collatz(collatz_num)
        aleady_found.add(collatz_num)

    print(j, counter, len(aleady_found))

    if counter > biggest_sequece:
        biggest_sequece = counter
        biggest_sequece_num = j
    

print(biggest_sequece_num)