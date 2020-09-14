from itertools import permutations

def find_nqueen(n=8, display=True):
    if n<8:
        raise Exception('n must be grater than or equal 8')
    sol=0
    cols = range(n)
    result = []
    for combo in permutations(cols):                      
        if n==len(set(combo[i]+i for i in cols))==len(set(combo[i]-i for i in cols)):
            sol += 1
            result.append(combo)
            if display:
                print('Solution {}: {}\n'.format(str(sol), str(combo)))
                print("\n".join(' o ' * i + ' X ' + ' o ' * (n-i-1) for i in combo) + "\n\n\n\n")
    
    return (sol, result)

if __name__ == '__main__':
    for i in range(8,11):
        solution_count, solutions = find_nqueen(i, False)
        print("Total solutions for N={}: {}".format(i, str(solution_count)))