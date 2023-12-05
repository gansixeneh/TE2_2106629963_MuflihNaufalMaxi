import time
from random import randint
import random
from memory_profiler import memory_usage
from Greedy import Greedy
from BranchBound import BB

class args:
    def __init__(self, universe, subsets, costs):
        self.universe = universe
        self.subsets = subsets
        self.costs = costs

def display_total_memory(func, A):
    memory_usages = memory_usage((display_total_running_time, (func, A)), max_iterations=1)
    print(f"Total memori yang digunakan: {max(memory_usages)} MB")

def display_total_running_time(func, A):
    start_time = time.time()
    print("Cost minimum yang diperoleh: ", end='')
    print(func(A.universe, A.subsets, A.costs)[0])
    end_time = time.time()
    print(f'Total waktu: {(end_time - start_time) * 1000} ms')

def find_total_memory(A):
    print("-------------- Greedy --------------")
    display_total_memory(Greedy, A)
    print()

    print("------------------- Branch & Bound -------------------")
    display_total_memory(BB, A)
    print()
    print()

def create_random_subset(N, subset_size):

    all_numbers = list(range(1, N + 1))
    random.shuffle(all_numbers)
    random_subset = all_numbers[:subset_size]

    return set(random_subset)

if __name__ == '__main__':
    for N in [20, 200, 2000]:
        for S_size in [10, 20, 40]:
            print("============================================================")

            print(f"N: {N}")
            print(f"Ukuran S: {S_size}")

            universe = [i for i in range(1, N+1)]
            universe = set(universe)
            subsets = []
            costs = []
            for _ in range(S_size-1):
                subsets.append(create_random_subset(N, randint(1, N)))
                costs.append(randint(1, 10000))
            
            last_set = set(universe)
            for i in universe:
                avail = False
                for j in range(S_size-1):
                    if i in subsets[j]:
                        avail = True
                
                if avail == False or randint(0, 1) == 1:
                    last_set.add(i)
            
            subsets.append(last_set)
            costs.append(randint(1, 10000))
            
            random.shuffle(subsets)

            A = args(universe, subsets, costs)

            find_total_memory(A)