# Publication strategy

The private repository keeps the complete internal lineage.

The public API_CELL branch is a clean orphan branch intended to expose only a lightweight API surface.

Recommended use:

1. Keep private internal repository private.
2. Use this branch as the export base.
3. Push this branch to a separate public repository if public release is required.
4. Do not expose private branch names, PKI paths, OAuth files, or internal runtime history in public release notes.

This branch is intentionally small and independent.
