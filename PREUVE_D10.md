# CERTIFICATE OF EXACT AFFINE DIMENSION 10 AND GRAPH SPECTRUM

## A. Conservative extension and rank

The pinned D09 configuration contains 14 labelled radius-one vertices, intrinsic affine rank 9, and 91 exact labelled squared distances. Embed these as `p_i'=(p_i,0)` and append the unit vector `p'_15=e_11`, orthogonal to every parent vector. Each of the 91 old distances is unchanged, and for all i in 1..14:

```
d(p'_i,p'_15)^2 = ||p'_i||² + ||p'_15||² - 2<p'_i,p'_15> = 1+1-0=2.
```

Thus 91+14=105 pairs. The full normalized histogram is `{4:6,7:2,8:74,9:3,10:10,12:6,13:2,16:2}`; the squared-distance sum at radius one is `887/4`.

Let `X` be the 15 x 11 exact storage-coordinate array, `D` the matrix of 105 labelled squared distances, and `H=I-11^T/15`. The centered squared-distance Gram matrix is `B=-H D H/2`. The exact symbolic code checks:

```
rank([p'_2-p'_1,...,p'_15-p'_1]) = 10
rank(B) = 10
B = (H X)(H X)^T   (exactly)
```

This last factorization proves `B` positive semidefinite, and its rank is fixed by the labelled metric. Hence the minimal possible Euclidean affine embedding dimension of *any* realization of **this exact labelled set of 105 distances** is 10. A display or ambient storage representation with 11 coordinates does not imply eleven intrinsic dimensions.

## B. Exact weighted-graph spectral recurrence

Place an illustrative equal-mass scalar oscillator at each point; choose all-pairs couplings `w_ij=1/d_ij²` and graph Laplacian `L`. The new vertex has 14 couplings, each exactly `1/2`, so

```
L_10 = [ L_9 + (1/2) I_14      -(1/2) 1  ]
       [ -(1/2) 1^T                 7    ]
```

For `chi_14(z)=det(z I-L_9)` and `chi_15(z)=det(z I-L_10)`:

```
chi_15(z)=z(z-15/2) chi_14(z-1/2)/(z-1/2).
```

From the pinned D09 identity `chi_14(z)=z(z-7)^3(z-13/2)^4 f_6(z-7/2)`, where `f_6(z)=chi_P7(z)/z`, follows

```
chi_15(z)=z(z-15/2)^4(z-7)^4 f_6(z-4).
```

The main verifier computes the entire characteristic polynomial of the **15 x 15** Laplacian by exact symbolic algebra and verifies this closed-form equality. It also checks `f_6(7/2)!=0` and `f_6(3)!=0`, guaranteeing **exact multiplicity 4** of the eigenvalue `15/2` and **exact multiplicity 4** of the eigenvalue `7`. The independent checker reconstructs the Laplacian from rational metric entries and proves multiplicities with direct characteristic polynomial derivatives.

This spectral result is limited to a **deliberately defined graph model** and is not experimental physics.

## C. Audit controls and open questions

The two independent programs verify the complete labelled matrix, all 91 prior distances, histogram, Gram rank, spectral roots and multipliers. Four counterchecks detect a corrupted distance, duplicated vertex, tilted non-orthogonal point and swapped labels whose multiset of distances would otherwise be unchanged.

Orthogonal embeddings and eigenvalue shifts on graph joins are known operations. This is a verified particular construction, not a demonstrated novel universal theorem. No experimental system or human peer review is claimed.
