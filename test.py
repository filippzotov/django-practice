import numexpr as ne
import itertools

nums = [45, 56, 13, 34]
perm_set = itertools.permutations(nums)

operators = ["+", "-", "*", "/", "%"]
for num in perm_set:
    for a in operators:
        for b in operators:
            for c in operators:
                op = f"{num[0]}{a}{num[1]}{b}{num[2]}{c}{num[3]}"
                if ne.evaluate(op) == 15:
                    print(op)
