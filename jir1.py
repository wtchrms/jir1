from sys import stdin, stdout

def NWD(x, y):
    while (y): x, y = y, x % y
    return x

def main():
    t = int(stdin.readline())
    while t != 0:
        a, b, d = map(int, stdin.readline().split())
        nwd=int(NWD(a,a+b))
        print("{:.0f}/{:.0f}".format(a / nwd, (a+b) / nwd))
        t = t - 1

main()
