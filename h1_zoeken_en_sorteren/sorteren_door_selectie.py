def selection_sort_vooraan(a):
    n = len(rij)
    for i in range(0, n-2):
        pos_min = i
        minimum = rij[i]
        for j in range(i+1, n-1):
            if rij[j] < minimum:
                pos_min = j
                minimum = rij[j]
        rij[i], rij[pos_min] = minimum, rij[i]
        print(rij)

def selection_sort(rij):
    n = len(rij)
    for i in range(n-1, 0, -1):
        pos_max = i
        maximum = rij[i]
        for j in range(i-1, -1, -1):
            if rij[j] > maximum:
                pos_max = j
                maximum = rij[j]
        rij[i], rij[pos_max] = maximum, rij[i]
        print(rij)



rij = [int(_) for _ in input().split()]
selection_sort(rij)