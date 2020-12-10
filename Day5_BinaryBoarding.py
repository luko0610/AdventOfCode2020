with open('./input_Day5.txt') as f:
    input = f.readlines()

results = []

#part 1
for line in input:
    beginSeat = 0
    endSeat = 127

    beginSeatColumn = 0
    endSeatColumn = 7

    for d in range(0, 7):
        if(line[d] == 'F'):
            endSeat -= int((endSeat - beginSeat + 1)/2)
        elif(line[d] ==  'B'):
            beginSeat += int((endSeat - beginSeat + 1)/2)

    for d in range(7, 10):
        if(line[d] == 'L'):
            endSeatColumn -= int((endSeatColumn - beginSeatColumn + 1)/2)
        elif(line[d] ==  'R'):
            beginSeatColumn += int((endSeatColumn - beginSeatColumn + 1)/2)
            
    results.append({ 'row':  endSeat, 'column': endSeatColumn, 'id': endSeat * 8 + endSeatColumn})

print('highest seat id ' + str(max(results, key=lambda x:x['id'])))
print('lowest seat id ' + str(min(results, key=lambda x:x['id'])))

# TODO: Make this more dynamic -> Get the full results at one run, without using output in code.
for r in range(0, 123):
    
    # normally row has 8 seats
    row = [d for d in results if d['row'] == r]

    # find row with exactly one missing seat
    if(len(row) == 7):
        print('seat missing!')
        print(row)

# according to above output row 66 / column 6 is missing
print('missing seat id ' + str(66 * 8 + 6))


   



        
