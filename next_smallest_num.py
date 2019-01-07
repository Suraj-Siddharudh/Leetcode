def sol(data):
    solution = []
    for i in range(len(data) - 1):
        for itr in range(i+1, len(data)):
            if data[itr] < data[i]:
                solution.append((data[i], data[itr]))
                break
    return solution


data = [6, 3, 12, 13, 5, 2]
print(sol(data))