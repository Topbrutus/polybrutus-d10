#!/usr/bin/env python3
"""Independent Polybrutus D10 verifier: rational metric and spectral roots.

Does not import the main D10 generator or parent generator. Starting from
seven canonical rational a,y,z coordinates with x=a*sqrt(3), then the
5-simplex vertex block and 3 new mutually orthogonal unit vertices,
reconstructs all 105 squared distances by a separate piecewise formula.
"""
import json,hashlib
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
doc=json.loads((ROOT/"results"/"certificate_d10.json").read_text(encoding="utf8"))
prev=json.loads((ROOT/"prior"/"certificate_d09.json").read_text(encoding="utf8"))
xyz=[
 (F(0),F(0),F(1)),
 (F(1,2),F(0),F(1,2)),
 (F(-1,4),F(3,4),F(1,2)),
 (F(-1,4),F(-3,4),F(1,2)),
 (F(0),F(0),F(-1)),
 (F(1,2),F(0),F(-1,2)),
 (F(-1,2),F(0),F(-1,2))
]
def d2(i,j):
    if i==j:return F(0)
    if i<7 and j<7:
        a,b,c=(xyz[i][k]-xyz[j][k] for k in range(3))
        return 3*a*a+b*b+c*c
    if 7<=i<12 and 7<=j<12:return F(5,2)
    return F(2)

edges=list(combinations(range(15),2))
indep={(i+1,j+1):d2(i,j) for i,j in edges}
rec={(int(x["i"]),int(x["j"])):F(x["d2"]) for x in doc["labelled_squared_distances"]}
assert len(indep)==105 and indep==rec
old={(int(x["i"]),int(x["j"])):F(x["d2"]) for x in prev["labelled_squared_distances"]}
assert len(old)==91 and all(indep[k]==v for k,v in old.items())
assert all(d2(i,14)==F(2) for i in range(14))
hist=Counter(4*d2(i,j) for i,j in edges)
assert hist==Counter({F(4):6,F(7):2,F(8):74,F(9):3,F(10):10,F(12):6,F(13):2,F(16):2})
assert sum(indep.values(),F(0))==F(887,4)
assert all(v>0 for v in indep.values())
D=sp.Matrix(15,15,lambda i,j:sp.Rational(d2(i,j).numerator,d2(i,j).denominator))
H=sp.eye(15)-sp.ones(15)/15
B=-H*D*H/2
assert B.rank()==10
D9=D[:14,:14];H9=sp.eye(14)-sp.ones(14)/14
assert (-H9*D9*H9/2).rank()==9

L=sp.zeros(15)
for i,j in edges:
    w=1/D[i,j]
    L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
z=sp.Symbol("z");chi=L.charpoly(z).as_expr()
for val,mult in [(sp.Rational(15,2),4),(sp.Integer(7),4)]:
    assert all(sp.simplify(sp.diff(chi,z,k).subs(z,val))==0 for k in range(mult))
    assert sp.simplify(sp.diff(chi,z,mult).subs(z,val))!=0
assert doc["affine_rank"]==doc["centered_gram_rank"]==10
assert doc["new_distances"]==14 and doc["parent_distances_preserved"]==91
print("INDEPENDENT D10 PASS: 105 rational labelled distances, 91 previous preserved, Gram rank 10")
print("INDEPENDENT SPECTRUM PASS: eigenvalue 15/2 x4, eigenvalue 7 x4")
print("CERTIFICATE_SHA256="+hashlib.sha256((ROOT/"results"/"certificate_d10.json").read_bytes()).hexdigest())
