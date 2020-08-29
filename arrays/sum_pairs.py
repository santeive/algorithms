def sum_pairs(lst, _suma):
    suma = 0
    list_sum = []
    count = {}
    t = ()

    for l in lst:
        for k in lst:
            suma = l + k
            if suma == _suma:
                t = t + (l,k)

    print(t)

def main():
    sum_pairs([1,3,2,2], 4)


main()

'''
https://www.w3resource.com/python-exercises/list/#EDITOR
https://adriann.github.io/programming_problems.html
http://users.csc.calpoly.edu/~jdalbey/103/Projects/ProgrammingPractice.html

'''
