# POLYBRUTUS 10D - Exact conservative distance completion and spectral transition

**Author and research responsibility:** Gabriel St-Pierre (Topbrutus), independent researcher.  
**Status:** Exact labelled Euclidean distance calculation; mathematical preprint, not peer reviewed.  
**AI disclosure:** OpenAI ChatGPT (Astra) substantially assisted symbolic verification, checker design, spectral model, source code and writing, and is not an author.

## Verified mathematical results (R=1)

- **15** labelled points and **105** pairwise squared distances; minimal Euclidean affine embedding dimension exactly **10**.
- The full preceding **Polybrutus 9D** configuration is preserved **91/91** labelled distances, without moving any original point.
- One new orthogonal radius-1 point generates exactly **14** new distances, all squared equal to **2**.
- Eight normalized classes for `k=4d²/R²`: `{4:6,7:2,8:74,9:3,10:10,12:6,13:2,16:2}`.
- Sum of all squared distances: `887/4`.
- Both coordinate-difference rank and centered squared-distance Gram rank equal **10**, with exact positive semidefinite factorization `B=(HX)(HX)^T`.
- **Ideal weighted Laplacian model:** eigenvalue `15/2` of exact multiplicity 4; eigenvalue `7` of exact multiplicity 4, proved by a closed-form characteristic polynomial and verified independently.

## Reproduce

```sh
python -m pip install sympy==1.14.0
python src/verify_d10.py
python tests/independent_d10.py
```

The independent verifier reconstructs 105 rational squared distances without importing the main generator. `prior/` contains source and immutable metric certificates from the **frozen D09 tag v0.1.0**, commit `3e435ea423e829d1b6cbc43fe8913e7338d4cb2c`.

## Files

- `src/verify_d10.py` - exact geometry, Gram factorization, rank, tamper tests, Laplacian spectrum.
- `tests/independent_d10.py` - independent rational metric and characteristic-polynomial multiplicity checks.
- `results/certificate_d10.json` - all 105 labelled squared distances and the exact computed invariants.
- `SPECIFICATION_D10.md`, `PREUVE_D10.md`, `PROVENANCE.md` - formal mathematical definitions and source chain.
- `publication/POLYBRUTUS_10D_NOTE.pdf` and `.md` - scientific research note with AI disclosure.
- `SHA256SUMS.txt` - versioned Git blob checksums, excluding its own content.

## Prior published work

- [Canonical seven-point Polybrutus specification](https://github.com/Topbrutus/polybrutus/blob/main/SPECIFICATION.md)
- [Polybrutus 7D DOI 10.5281/zenodo.24407952](https://doi.org/10.5281/zenodo.24407952)
- [Polybrutus 8D DOI 10.5281/zenodo.24408344](https://doi.org/10.5281/zenodo.24408344)
- [Polybrutus 9D DOI 10.5281/zenodo.24408448](https://doi.org/10.5281/zenodo.24408448)
- [Immutable D09 source tag](https://github.com/Topbrutus/polybrutus-d09/tree/v0.1.0)

**Scientific limits:** Orthogonal completion is established mathematics. The 'dimension' is a minimal mathematical affine embedding dimension, not a new physical dimension; the selected oscillator graph is an ideal mathematical model, not a laboratory measurement. No novel general theorem or particle claim is made. The source code is MIT licensed; the research paper is CC BY 4.0.
