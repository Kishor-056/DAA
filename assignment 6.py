
# 1
def t(c):
    k = c + 273.15
    f = c * 1.8 + 32
    return [k, f]

c = 25.0
print("1:")
print(t(c))

# 2
import math

def l(a, k):
    def g(x, y):
        while y:
            x, y = y, x % y
        return x

    def lcm(x, y):
        return (x * y) // g(x, y)

    n = len(a)
    c = 0
    for i in range(n):
        l = 1
        for j in range(i, n):
            l = lcm(l, a[j])
            if l == k:
                c += 1
            elif l > k:
                break
    return c

a = [2, 3, 4, 6]
k = 6
print("2:")
print(l(a, k))

# 3
from collections import deque, defaultdict
class T:
    def _init_(self, v=0, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r
def o(r):
    if not r:
        return 0
    q = deque([r])
    c = 0
    while q:
        n = len(q)
        v = []
        for _ in range(n):
            n = q.popleft()
            v.append(n.v)
            if n.l:
                q.append(n.l)
            if n.r:
                q.append(n.r)
        if v != sorted(v):
            p = {v[i]: i for i in range(len(v))}
            s = sorted(v)
            for i in range(len(v)):
                while p[s[i]] != i:
                    p[v[i]], p[v[p[s[i]]]] = p[v[p[s[i]]]], p[v[i]]
                    v[i], v[p[s[i]]] = v[p[s[i]]], v[i]
                    c += 1
    return c
r = T(1, T(4, T(7), T(6)), T(3, T(8), T(5)))
print("3:")
print(o(r))

# 4
def p(s, k):
    def is_palindrome(x):
        return x == x[::-1]

    n = len(s)
    dp = [0] * (n + 1)
    for i in range(n - k + 1):
        for j in range(i + k, n + 1):
            if is_palindrome(s[i:j]):
                dp[j] = max(dp[j], dp[i] + 1)
    return max(dp)

s = "abacdc"
k = 2
print("4:")
print(p(s, k))

# 5
from heapq import heappop, heappush
import sys
def a(n, r, c, k):
    g = defaultdict(list)
    for u, v, w in r:
        g[u].append((v, w))
        g[v].append((u, w))
    def dijkstra(s):
        h = [(0, s)]
        dist = [sys.maxsize] * n
        dist[s] = 0
        while h:
            d, u = heappop(h)
            if d > dist[u]:
                continue
            for v, w in g[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heappush(h, (dist[v], v))
        return dist
    res = []
    for i in range(n):
        dist = dijkstra(i)
        min_cost = sys.maxsize
        for j in range(n):
            min_cost = min(min_cost, dist[j] + c[j] + dist[j] * k)
        res.append(min_cost)
    return res
n = 4
r = [(0, 1, 10), (1, 2, 10), (2, 3, 10), (3, 0, 10)]
c = [1, 2, 3, 4]
k = 2
print("5:")
print(a(n, r, c, k))

# 7
def t(a):
    n = len(a)
    c = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if a[i] != a[j] and a[i] != a[k] and a[j] != a[k]:
                    c += 1
    return c

a = [1, 2, 3, 4]
print("7:")
print(t(a))

# 8
class N:
    def _init_(self, x):
        self.v = x
        self.l = None
        self.r = None
def bst_insert(r, v):
    if not r:
        return N(v)
    if v < r.v:
        r.l = bst_insert(r.l, v)
    else:
        r.r = bst_insert(r.r, v)
    return r
def find_closest_nodes(r, q):
    def inorder(n):
        return inorder(n.l) + [n.v] + inorder(n.r) if n else []
    def find_closest(val):
        l, r = -1, -1
        for v in vals:
            if v <= val:
                l = v
            if v >= val and r == -1:
                r = v
        return [l, r]
    vals = inorder(r)
    return [find_closest(x) for x in q]
r = N(6)
for v in [2, 13, 1, 4, 9, 15, 14]:
    bst_insert(r, v)
q = [3, 7, 10]
print("8:")
print(find_closest_nodes(r, q))

# 9
def fuel_cost(r, s):
    from collections import defaultdict, deque
    g = defaultdict(list)
    for u, v in r:
        g[u].append(v)
        g[v].append(u)
    def bfs():
        q = deque([0])
        visited = {0}
        cost = 0
        while q:
            for _ in range(len(q)):
                u = q.popleft()
                for v in g[u]:
                    if v not in visited:
                        q.append(v)
                        visited.add(v)
                        cost += 1
        return cost
    return bfs()
r = [(0, 1), (1, 2), (2, 3), (3, 0)]
s = 2
print("9:")
print(fuel_cost(r, s))

# 10
def b(s, k, m):
    p = {'2', '3', '5', '7'}
    def is_beautiful(x):
        return x[0] in p and x[-1] not in p
    n = len(s)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(k + 1):
            if j > 0 and i >= m and is_beautiful(s[i - m:i]):
                dp[i][j] = (dp[i][j] + dp[i - m][j - 1]) % (10**9 + 7)
            dp[i][j] = (dp[i][j] + dp[i - 1][j]) % (10**9 + 7)
    return dp[n][k]
s = "2357"
k = 2
m = 2
print("10:")
print(b(s, k, m))
