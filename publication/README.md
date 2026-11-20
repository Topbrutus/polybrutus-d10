# Polybrutus D10 - Publication package

The computational mathematical preprint is available as PDF and Markdown with explicit AI disclosure, author attribution, provenance, unreviewed status and precise scope.

The release is constructed in two phases: (1) private GitHub repository, exact tests and CI, fixed verified tag; (2) a **unique controlled direct-API Zenodo draft**, containing a Git-archive ZIP made *from that fixed tag* plus the PDF and the exact JSON certificate. No simultaneous automatic GitHub-Zenodo archive should be enabled, to prevent duplicates.

Only after matching file SHA-256, metadata, public repository tag and independent tests is Zenodo publication allowed. Public DOI and GitHub links must be recorded in README, CITATION.cff, manifest and Memoria. Never modify the frozen scientific source tag after publication.
