for i in range(int(input())):
    print("${0:.2f}".format(sum(map(lambda x: x[0]*x[1], zip([350.34, 230.90, 190.55, 125.30, 180.90], map(int, input().split()))))))
