def Greedy(universe, subsets, costs):
    cost = 0
    covered = set()
    cover = [0 for x in range(len(subsets))]
    while covered != universe:
        max_val, subset = len(subsets[0]-covered)/costs[0], subsets[0]
        index = 0
        for i in range(len(subsets)):
            new_val = len(subsets[i]-covered)/costs[i]
            if new_val > max_val:
                index = i
                subset = subsets[i]
                max_val = new_val

        cover[index] = 1
        cost += costs[index]
        covered |= subset

    return cost, cover
