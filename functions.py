import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

def plot_function(x_vals: list, y_vals: list, plt_xlbl: str, plt_ylbl: str, plt_name: str=None, plt_size: tuple=(16, 8), plt_path: str='img/'):

    if plt_name == None:
        plt_name = plt_xlbl + "_vs_" + plt_ylbl
    else:
        plt_name = plt_name

    plt.figure(figsize=plt_size)
    plt.xlabel(plt_xlbl)
    plt.ylabel(plt_ylbl)
    plt.title(plt_name)
    plt.plot(x_vals, y_vals)
    plt.grid(True)
    plt.savefig(plt_path + plt_name + '.png')
    plt.show()

# Persistence

def persistence(n, counter=0):

    if len(str(n)) == 1:
        print(n)

        return 'DONE in 1 Step'

    result = 1
    digits = [int(i) for i in str(n)]
    for j in digits:
        result *= j
    counter += 1

    print(result, counter)
    persistence(result, counter)

# Truncation of Primes

def is_prime(n):
    for i in range(2, int(n // 2) + 1):
        if n % i == 0:
            return False
    return n <= 1 or n % 1 > 0

def truncate_list(n):
    return [n * 10 + i for i in range(0, 10)]

def truncate(n):
    primes = []
    print(truncate_list(n))
    for i in truncate_list(n):
        if is_prime(i):
            primes.append(i)
    print(primes)
    try:
        choice = random.choice(primes)
    except IndexError:
        print("No Primes Left")
        print("Max # of digits are: ")
    else:
        truncate(choice)

# Perfect and Triperfect Numbers

def is_perfect_number(n):
    def factors():

        factor_list = []
        for i in range(1, n+1):
            if (n % i) == 0:
                factor_list.append(i)
                
        return factor_list

    def new_factor_list():

        fact_list = factors()[:-1]

        return fact_list
    
    num_factors = new_factor_list()
    sum_of_factors = sum(num_factors)
    return sum_of_factors == n

def is_triperfect_number(n):
    def factor():
        factor_list = []
        for i in range(1, n + 1):
            if (n % i) == 0:
                factor_list.append(i)
        return factor_list
    
    factor_list = factor()
    return sum(factor_list) == 3 * n

# Recaman Sequence

def semi_circle(radius: float, shift: float, color: str, sign=1, n_points=100):
    
    x = np.linspace(-radius+shift, radius+shift, n_points)
    y = []
    for i in x:
        y.append(sign * np.sqrt(radius ** 2 - (i - shift) ** 2))
            
    Y = plt.plot(x, y, c=color)
    
def recaman(n: int): 
  
    arr = [0] * n 
    for i in range(1, n): 
        curr = arr[i-1] - i 
        for j in range(0, i): 
            if ((arr[j] == curr) or curr < 0): 
                curr = arr[i-1] + i 
                break
        arr[i] = curr
        
    return arr

def recaman_graph(num_loops: int, color: str):
    A = recaman(num_loops)
    sign = 1
    for i in range(len(A) - 1):
        
        sign = sign
        semi_circle((A[i+1] - A[i])*0.5, (A[i+1] - A[i]) * 0.5 + A[i], color, sign)
        sign *= -1
        
    plt.savefig('/img/recaman_seq_' + str(num_loops) + '.png')
    plt.show()

# Serpinsky Triangle

class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    
def roll():
    return np.random.randint(1, 4)

def get_distance(trace, main):
    return ((trace.x - main.x), (trace.y - main.y))

def rel_loc(distance):
    return [int(distance[0] >= 0), int(distance[1] >= 0)]

def generate_serpinsky(resolution: int=10000, vertices: int=3):
    main_p = []
    plt.figure()
    for i in range(vertices):
        main_p.append(Point(np.random.rand(), np.random.rand(), 'r'))
    
    for i in range(vertices):
        plt.scatter(main_p[i].x, main_p[i].y, c=main_p[i].color)
        plt.annotate(i, (main_p[i].x, main_p[i].y))

    trace_p = Point(np.random.rand(), np.random.rand(), 'black')
    plt.scatter(trace_p.x, trace_p.y, c=trace_p.color)
    new_p = []

    for i in range(10000):
        roll_dice = roll()
        if roll_dice in [1, 2, 3]:
            new_coords = get_distance(trace_p, main_p[roll_dice - 1])

        relative_loc = rel_loc(new_coords)

        if relative_loc == [1, 1]:
            new_p.append(Point(trace_p.x - new_coords[0]/2, trace_p.y - new_coords[1]/2, 'b'))
        elif relative_loc == [0, 0]:
            new_p.append(Point(trace_p.x - new_coords[0]/2, trace_p.y - new_coords[1]/2, 'b'))
        elif relative_loc == [1, 0]:
            new_p.append(Point(trace_p.x - new_coords[0]/2, trace_p.y - new_coords[1]/2, 'b'))
        elif relative_loc == [0, 1]:
            new_p.append(Point(trace_p.x - new_coords[0]/2, trace_p.y - new_coords[1]/2, 'b'))

        trace_p = new_p[i]
        plt.scatter(new_p[i].x, new_p[i].y, c=new_p[i].color, s=1)
        
    plt.show()

# Amazing Graphs

def dec_to_bin(n: int, reversed: bool=False):
    binary = bin(n)[2:]
    return binary[::-1] if reversed else binary

def bin_to_dec(bin_string: str, reversed: bool=True):

    number = 0

    if reversed:
        bin_string = bin_string[::-1]
    
    for i, num in enumerate(bin_string):
        if num == '1':
            number += 2 ** i
    
    return number

def get_primes():

    with open('data/10000primes.txt', 'r') as fobj:
        prime_lst = [int(num) for num in fobj.read().split()]

    return prime_lst

def generate_prime_trapz():

    prime_lst = get_primes()
    bin_lst = [dec_to_bin(i) for i in prime_lst]
    rev_bin_lst = [dec_to_bin(i, reversed=True) for i in prime_lst]
    diff_lst = [prime_lst[i] - bin_to_dec(rev_bin_lst[i]) for i in range(10000)]

    df_binprimes = pd.DataFrame({'primes':prime_lst, 'bin_primes': bin_lst, 'rev_bin_primes': rev_bin_lst, 'diff': diff_lst})

    plt.figure()
    plt.scatter(df_binprimes['primes'], df_binprimes['diff'], c='black', s=0.1)
    plt.show()

# Forest Fire Sequence

def generate_forest_fires(num_limit: int=10000, document: bool=False, marker_size: float=0.5):

    """
    *Generates a graph of the forest fire sequence (A229037)
    *num_limit and document set at default values, recommended for low-performance computers
    *marker_size = 0.5 is optimum for better looking graph
    *Setting bool document = True makes the function print the algorithmic procedure at each step
    *Outputs ff(num_limit) array
    """
    ff = [1, 1]
    run = True
    counter = 0
    trial = 1

    while run:

        klist = 0
        yes_count = 0
        ff.append(trial)

        if len(ff) % 2 == 0:
            klist = (math.floor((len(ff) - 1) / 2)) + 1
        else:
            klist = (math.floor(len(ff) / 2)) + 1

        for k in range(1, klist):
            
            last_ind = len(ff) - 1
            if document:
                print("--------")
                print("ff[last_ind] = " + str(ff[last_ind]))
                print("ff[last_ind - k] = " + str(ff[last_ind - k]))
                print("ff[last_ind - 2 * k] = " + str(ff[last_ind - 2 * k]))
                
            if (ff[last_ind] - ff[last_ind - k]) == (ff[last_ind - k] - ff[last_ind - (2 * k)]):
                if document:
                    print("no" + " -> difference(" + str(ff[last_ind] - ff[last_ind - k]) + "," + str(ff[last_ind - k] - ff[last_ind - (2 * k)]) + ")")
                ff = ff[:len(ff) - 1]
                trial += 1
                break
            elif (ff[last_ind] - ff[last_ind - k]) != (ff[last_ind - k] - ff[last_ind - (2 * k)]):
                if document:
                    print("yes" + " -> difference(" + str(ff[last_ind] - ff[last_ind - k]) + "," + str(ff[last_ind - k] - ff[last_ind - (2 * k)]) + ")")
                yes_count += 1
                if yes_count == klist - 1:   
                    counter += 1
                    if document:
                        print(counter)
                    trial = 1
                    break
                
        if counter == 10000:
            print("Done!")
            run = False

    plt.scatter(range(len(ff)), ff, s=marker_size)
    plt.savefig('/img/forest_fire.png')
    plt.show()

    return ff