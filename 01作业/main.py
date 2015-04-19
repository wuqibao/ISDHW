for a in range(1,10):
        for b in range(a,10):
            s="{0}*{1}={2:>2}".format(a,b,a*b)
            print(s,end="  ")
        print()
       
