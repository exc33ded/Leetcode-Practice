f = open("user.out", 'w')
for n, t in zip(stdin, stdin):
    n, t = n[1:-2].split(','), int(t.rstrip())
    r, l, z = len(n)-1, 0, -1
    while l <= r:
        m = ((r-l)//2)+l
        if int(n[m])>t:
            r=m-1
        elif int(n[m])<t:
            l=m+1
        else:
            z = m
            break
    print(z, file=f)
exit(0)
            