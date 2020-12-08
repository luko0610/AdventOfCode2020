with open('./input_Day1.txt') as f:
    input = f.readlines()
    input = list(map(int, input))

# part 1
for k in range(len(input)):
    for l in range(len(input)):
        if k != l and input[k] + input[l] == 2020:
            print('Result: ' + str(input[k] * input[l]))
            break


# part 2
for k in range(len(input)):
    for l in range(len(input)):
        for m in range(len(input)):
            if input[k] + input[l] + input[m] == 2020:
                print('Result: ' + str(input[k] * input[l] * input[m]))
                break
    
