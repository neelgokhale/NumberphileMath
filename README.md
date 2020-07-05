# Numberphile Math
I love [Numberphile](https://www.youtube.com/channel/UCoxcjq-8xIDTYp3uz647V5A)! These functions were coded in my feeble attempts to generate a python package filled with math-related madness (and sometimes, beauty). 

Disclaimer: I know nothing about Number Theory...

## Table of Contents

<!--ts-->
- [Persistence](#persistence)
- [Prime Truncation](#prime-truncation)
- [Perfect Numbers](#perfect-numbers)
- [Triperfect Numbers](#triperfect-numbers)
- [Sierpiński Triangle through Pseudo-Randomness](#sierpiński-triangle-through-pseudo-randomness)
- [Recaman Sequence](#recaman-sequence)
- [Amazing Graphs: Prime Number Trapezoids](#amazing-graphs-prime-number-trapezoids)
<!--te-->

## Persistence

Well, multiplicative persistence to be precise. This function multiplies a given number's digits until the resulting product is a single digit value. The number with the most multiplicative persistence is `277777788888899`, with `11` iterations.

```python
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
    
```


```python
persistence(2227788888889)
```

    7398752256 1
    6350400 2
    0 3
    0
    
## Prime Truncation

This one's a bit silly. So you start with any given number, and if that number is prime, you truncate all the numbers from `0` to `9` to this number. Then check if that new number is prime, create a list of those new prime numbers and... repeat the process until you cannot make another prime number. Yeah, definately wierd.

```python
import random
def is_prime(n):
    if n <= 1 or n % 1 > 0 or n == 4:
        return False
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True

def truncate_list(n):
    trunc_list = []
    for i in range(0, 10):
        trunc_list.append(int(str(n) + str(i)))
    return trunc_list

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
```


```python
truncate(4)
```

    [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
    [41, 43, 47]
    [410, 411, 412, 413, 414, 415, 416, 417, 418, 419]
    [419]
    [4190, 4191, 4192, 4193, 4194, 4195, 4196, 4197, 4198, 4199]
    []
    No Primes Left
    Max # of digits are: 
    
## Perfect Numbers

The factors of these numbers add up to equal that number.

```python
def is_perfect_number(n):
    bool_perfect = False
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
    if sum_of_factors == n:
        bool_perfect = True
        return bool_perfect
    else:
        bool_perfect = False
        return bool_perfect
        
```

```python
perfect_factor_list = []
for i in range(1000):
    if is_perfect_number(i):
        perfect_factor_list.append(i)

perfect_factor_list
```

    [0, 6, 28, 496]


## Triperfect Numbers

```python
def is_triperfect_number(n):
    bool_triperfect = False
    
    def factor():
        factor_list = []
        for i in range(1, n + 1):
            if (n % i) == 0:
                factor_list.append(i)
        return factor_list
    
    factor_list = factor()
    if sum(factor_list) == 3 * n:
        bool_triperfect = True
        return bool_triperfect
    else:
        bool_triperfect == False
        return bool_triperfect
        
```


```python
is_triperfect_number(120)
```

    True

## Sierpiński Triangle through Pseudo-Randomness

Ok this one is crazy... I cannot fully explain how it works but the following is the basic algorithm:
1. Generate `3` main points at random locations (red)
2. Generate `1`st trace point at random location
3. roll dice
   - if dice at `1, 2` -> go to main point `0`, `3, 4` -> main point `1`, and `5, 6` -> main point `2`
   - find distance between trace point and main point
   - find relative loc based on distance
   - find new point
4. Set trace point as new point
5. append new point to new point array
6. plot scatter with updated data


```python
import matplotlib.pyplot as plt
import numpy as np

class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    
def roll():
    return np.random.randint(1, 7)

def get_distance(trace, main):
    return ((trace.x - main.x), (trace.y - main.y))

def rel_loc(distance):
    dist_loc = [1, 1]
    if distance[0] < 0:
        dist_loc[0] = 0
    else:
        dist_loc[0] = 1
        
    if distance[1] < 0:
        dist_loc[1] = 0
    else:
        dist_loc[1] = 1
    
    return dist_loc

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
        if (roll_dice == 1):
            new_coords = get_distance(trace_p, main_p[0])
        elif (roll_dice == 2):
            new_coords = get_distance(trace_p, main_p[1])
        elif (roll_dice == 3):
            new_coords = get_distance(trace_p, main_p[2])

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

```

![png](/img/output_10_0.png)


![png](/img/output_11_0.png)

## Recaman Sequence
Here is a seemingly ordered, yet chaotic sequence. The algorithm to follow is:

```
Let a(n) denote the nth term of the sequence

If n > 0 and n not in a:
    a(n) = a(n - 1) - n
else:
    a(n) = a(n - 1) + n
```
This produces a beautiful graph.


```python
def semi_circle(radius: float, shift: float, color: str, sign=1, n_points=100):
    
    x = np.linspace(-radius+shift, radius+shift, n_points)
    y = []
    for i in x:
        y.append(sign * np.sqrt(radius ** 2 - (i - shift) ** 2))
            
    Y = plt.plot(x, y, c=color)
    
def recaman(n: int): 
  
    arr = [0] * n 
    arr[0] = 0
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
    plt.savefig('recaman_seq_' + str(num_loops) + '.png')
    

```

![png](/img/output_17_0.png)


## Amazing Graphs: Prime Number Trapezoids

Using a simple process (i.e. take a prime number, find its binary representation, flip it and find the decimal difference), I mapped the first `10000` prime numbers and their binary differences into a scatter plot. The result is kinda cool!

```python

def dec_to_bin(n: int, reversed: bool=False):

    binary = bin(n)[2:]
    if reversed:
        return binary[::-1]
    else:
        return binary

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

```

![png](/img/prime_trapz.png)
