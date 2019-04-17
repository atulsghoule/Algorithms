def tower(n,from_ = 'A',to_ = 'B',inter_ = 'C'):
    if n==1:
        print "Move disk 1 from %c to rod %c "%(from_,to_)
        return 
    tower(n-1,from_,inter_,to_)
    print "Move disk %d from %c to rod %c "%(n,from_,to_)
    tower(n-1,inter_,to_,from_)
tower(14)
