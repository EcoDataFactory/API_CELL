# GAM_py runtime import contract

This repository intentionally keeps the legacy GAM import model.

Runtime entrypoint:

    GAM_py/src/bin/gam

The wrapper exports:

    PYTHONPATH="$SRC/gam:$SRC/vendor:$SRC${PYTHONPATH:+:$PYTHONPATH}"

This path order is required:

1. $SRC/gam
   - resolves gamlib
   - contains gam.py
   - contains gam_api.py

2. $SRC/vendor
   - resolves vendored gdata

3. $SRC
   - resolves vendored legacy atom

Current package roots:

    GAM_py/src/
    ├── atom/              # import atom
    ├── gam/
    │   ├── gam.py
    │   ├── gam_api.py
    │   └── gamlib/        # import gamlib
    └── vendor/
        └── gdata/         # import gdata

The following absolute imports are intentional:

    from gamlib import ...
    import atom
    import atom.*
    import gdata
    import gdata.*

Do not rewrite atom or gdata imports unless doing a controlled namespace migration with runtime tests.

Required validation:

    PYTHONPATH="$PWD/GAM_py/src/gam:$PWD/GAM_py/src/vendor:$PWD/GAM_py/src" python -c "import atom, gdata, gamlib; print(atom.__file__); print(gdata.__file__); print(gamlib.__file__)"

    GAM_py/src/bin/gam status
    GAM_py/src/bin/gam api status
    GAM_py/src/bin/gam live --version
