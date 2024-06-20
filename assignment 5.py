
#1
class N:
    def _init_(s, v):
        s.v = v
        s.c ,s.s= [],0
def b_t(n, e, v):
    t = [N(v[i]) for i in range(n)]
    for x, y in e:
        t[x].c.append(t[y])
        t[y].c.append(t[x])
    return t[0]
def s_s(n, p):
    s = n.v
    for c in n.c:
        if c == p:
            continue
        s += s_s(c, n)
    n.s = s
    return s
def d(n, p, t, s):
    m = 0
    for c in n.c:
        if c == p:
            continue
        m = max(m, d(c, n, t, s))
    if n != p:
        for x in s:
            m = max(m, (t - n.s) ^ x)
        s.add(n.s)
    return m
def x_t(n, e, v):
    t = b_t(n, e, v)
    t_s = s_s(t, None)
    return d(t, None, t_s, set())
n = 6
e = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]]
v = [2, 8, 3, 6, 2, 5]
print(x_t(n, e, v))  

#3
def m_c(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return n // 2
    else:
        return n
print(m_c(4))

#4
def d_b_r_c(grid):
    rows = len(grid)
    cols = len(grid[0])
    row_ones = [sum(row) for row in grid]
    col_ones = [sum(grid[i][j] for i in range(rows)) for j in range(cols)]
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            ones = row_ones[i] + col_ones[j] - grid[i][j]
            zeros = (rows - row_ones[i]) + (cols - col_ones[j]) - (1 - grid[i][j])
            result[i][j] = ones - zeros
    return result
grid = [[0, 1, 1],[1, 0, 1],[0, 0, 1]]
print(d_b_r_c(grid))  

#5
def m_p(c):
    y = c.count('Y')
    n = len(c) - y
    min_p = n
    p = 0
    m_t = 0
    for i, ch in enumerate(c):
        if ch == 'Y':
            p -= 1
        else:
            p += 1
        if p < min_p:
            min_p = p
            m_t = i + 1
    return m_t
print(m_p("YYNY"))  

#6
def c_p_s(s):
    MOD = 10**9 + 7
    n = len(s)
    dp = [[[0] * 6 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i][1] = 1
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if s[i] == s[j]:
                for k in range(1, 5):
                    dp[i][j][k + 1] = (dp[i][j][k + 1] + dp[i + 1][j - 1][k]) % MOD
            for k in range(1, 6):
                dp[i][j][k] = (dp[i][j][k] + dp[i + 1][j][k] + dp[i][j - 1][k] - dp[i + 1][j - 1][k]) % MOD
    
    return dp[0][n - 1][5]
print(c_p_s("103301"))

#7
def p_i(n):
    t = (n * (n + 1)) // 2
    s = 0
    for i in range(1, n + 1):
        s += i
        if s == t - s + i:
            return i
    return -1
print(p_i(8))

#8
def a_c(s, t):
    i = 0
    for c in s:
        if i < len(t) and c == t[i]:
            i += 1
    return len(t) - i
print(a_c("coaching", "coding"))

#9
class L:
    def _init_(s, v=0, n=None):
        s.v = v
        s.n = n
def r_n(h):
    d = L(0)
    d.n = h
    s = []
    c = d
    while c:
        while s and s[-1].v < c.v:
            s.pop()
        s.append(c)
        c = c.n
    for i in range(len(s) - 1):
        s[i].n = s[i + 1]
    s[-1].n = None
    return d.n
def l_t_a(l):
    a = []
    while l:
        a.append(l.v)
        l = l.n
    return a
h = L(5, L(2, L(13, L(3, L(8)))))
r = r_n(h)
print(l_t_a(r))  

#10
def c_m_k(a, k):
    n = len(a)
    m_i = a.index(k)
    d = {0: 1}
    b = 0
    c = 0
    for i in range(m_i, n):
        if a[i] < k:
            b -= 1
        elif a[i] > k:
            b += 1
        c += d.get(b, 0) + d.get(b - 1, 0)
        d[b] = d.get(b, 0) + 1
    d = {0: 1}
    b = 0
    for i in range(m_i - 1, -1, -1):
        if a[i] < k:
            b -= 1
        elif a[i] > k:
            b += 1
        c += d.get(-b, 0) + d.get(-b - 1, 0)
        d[-b] = d.get(-b, 0) + 1
    return c
print(c_m_k([3, 2, 1, 4, 5], 4))
