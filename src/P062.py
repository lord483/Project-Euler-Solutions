from collections import defaultdict
if __name__ == "__main__":
    check = 5
    cubes = defaultdict(list)
    for i in range(10**5):
        sc = [c for c in str(i**3)]
        sc.sort()
        k = "".join(sc)
        cubes[k].append(i)
    res = []
    for k in cubes.keys():
        if len(cubes[k]) == check:
            res.append(min(cubes[k]))

    r = min(res)
    print(r , " ", r**3)
