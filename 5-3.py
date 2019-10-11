def check_fermat(a, b, c, n):
    return n > 2 and pow(a, n) + pow(b, n) == pow(c, n)

inputs = []
for ch in ['a', 'b', 'c', 'n']:
    tmp = input(f'Enter {ch}: ')
    try:
        inputs.append(int(tmp))
    except:
        raise Exception('You must input a integer!') 

print(check_fermat(inputs[0], inputs[1], inputs[2], inputs[3]))
