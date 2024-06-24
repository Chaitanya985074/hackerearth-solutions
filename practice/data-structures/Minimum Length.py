Problem link
https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/minimum-length-4-945227e2/

Solution
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        l, r = 0, n - 1
        while l <= r and a[l] == b[l]:
            l += 1
        while r >= l and a[r] == b[r]:
            r -= 1
        print(r - l + 1)

if __name__ == "__main__":
    main()
