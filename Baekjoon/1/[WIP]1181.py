print(*sorted(set([input()for i in range(int(input()))]),key=lambda l:sum(map(ord,l))),sep='\n',end='')
