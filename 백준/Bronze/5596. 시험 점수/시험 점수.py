na, nb, nc, nd = map(int, input().split())
ns = na + nb + nc + nd
ma, mb, mc, md = map(int, input().split())
ms = ma + mb + mc + md
a = [ns, ms]
print(max(a))