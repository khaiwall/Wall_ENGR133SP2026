import math
import statistics
def main():

    a=8
    print(a)

    b=math.pow(3, (a/3))
    print(b)

    c = math.cos(math.pow(b, (1/2)))
    c = math.cos(math.sqrt(b))
    print(c)

    d = math.floor(13*c)
    print(d)

    e = 613%d
    print(e)

    l = [a,b,c,d,e]
    m= statistics.mean(l)
    M= statistics.median(l)
    r= max(l) - min(l)
    MX = max(l)
    stdv = statistics.stdev(l)

    print(m)
    print(M)
    print(MX)
    print(r)
    print(stdv)



if __name__ == "__main__":
    main()