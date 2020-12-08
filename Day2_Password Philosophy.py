def parsePolicy(policy):
    split = policy.split(' ')
    begin = int(split[0].split('-')[0])
    end = int(split[0].split('-')[1])
    char = split[1]
    return (begin, end, char)

with open('./input_Day2.txt') as f:
    input = f.readlines()

validPolicy1 = 0
validPolicy2 = 0

for k in range(len(input)):
    split = input[k].split(':')
    policy = split[0]
    password = split[1].strip()
    begin, end, char = parsePolicy(policy)
    count = password.count(char);

    # policy part 1
    if(count >= begin and count <= end):
        validPolicy1 += 1

    # policy part 2
    if(password[begin - 1] == char and password[end - 1] != char or password[end - 1] == char and password[begin - 1] != char):
        validPolicy2 += 1


print(str(validPolicy1) + ' passwords are valid according to policy 1.')
print(str(validPolicy2) + ' passwords are valid according to policy 2.')


