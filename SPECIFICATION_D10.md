# POLYBRUTUS D10 - Exact construction specification

**Source of truth:** Polybrutus D09 GitHub tag `v0.1.0`, commit `3e435ea423e829d1b6cbc43fe8913e7338d4cb2c`, previously published under DOI `10.5281/zenodo.24408448`.

## Coordinates

In a normalized radius `R=1` representation, let `p_1,...,p_14` denote the exact D09 points in ten storage coordinates, which include a one-dimensional simplex constraint. For each i, set `p_i'=(p_i,0)`; append `p_15'=e_11=(0,...,0,1)`.

The first fourteen points remain unchanged. The new vertex is orthogonal to all preceding point vectors and is on the radius-one sphere. Scale all coordinates by arbitrary `R>0` to obtain the general model.

- Storage representation: **11** coordinates subject to one fixed linear constraint.
- Intrinsic affine rank: **10**.
- Total points: **15**.
- Labelled unordered pairs: **105**.
- Preserved previous metric: **91/91** squared labelled distances.
- New squared distances: **14**, all exactly `2R²`.

## Normalized distance family

For `k=4d²/R²`:

| k | 4 | 7 | 8 | 9 | 10 | 12 | 13 | 16 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Multiplicity | 6 | 2 | **74** | 3 | 10 | 6 | 2 | 2 |

Sum of all squared distances is `887 R²/4`. For radius 1, the centroid in the 11 storage slots is `(0,0,1/30,0,0,0,0,0,1/15,1/15,1/15)`.

## Mathematical-model spectrum

Choose ideal scalar oscillators and complete graph weights `w_ij=R²/d²_ij`. The D10 normalized Laplacian satisfies

```
L_10 = [ L_9 + (1/2) I_14      -(1/2) 1  ]
       [ -(1/2) 1^T                7     ]
```

Its exact characteristic polynomial is:

```
chi_15(z) = z (z-15/2)^4 (z-7)^4 f_6(z-4)
```

where `f_6(z)=chi_{P7}(z)/z` is the six-nonzero-mode factor of the canonical seven-point graph's ideal weighted Laplacian.

**No experimental observations, new fundamental physical dimensions or generalized novelty claims.**
