# Agent Instructions

This repository packages the upstream `melonDS` emulator for Fedora COPR.

## Scope And Safety

- Keep edits minimal and packaging-focused.
- Do not commit or track generated RPM build outputs from `BUILD/`, `BUILDROOT/`, `RPMS/`, `SRPMS/`, `SOURCES/melonDS-*.tar.gz`, `tmp/`, or `*.log`.
- Preserve the existing org-mode README style when editing `README.org`; use `~code~` or `=literal=` consistently with nearby text.
- Prefer adding focused packaging notes to `TROUBLESHOOTING.org` instead of expanding this agent instruction file.

## Upstream Version Discipline

- Before building or submitting to COPR, run:

  ```sh
  make check-upstream-version
  ```

- If upstream has a newer GitHub release tag, update `Version:` and `%changelog` in `SPECS/melonDS.spec` before creating an SRPM.
- Build COPR upload artifacts with `make srpm`; do not hand-write the SRPM command unless diagnosing the Makefile.

## COPR Workflow

- COPR project: `archjun/melonDS`
- Fedora 44 chroots expected for this task:
  - `fedora-44-aarch64`
  - `fedora-44-x86_64`
- Use explicit chroots when submitting Fedora-version-specific builds, for example:

  ```sh
  copr-cli build archjun/melonDS \
    -r fedora-44-aarch64 \
    -r fedora-44-x86_64 \
    SRPMS/melonDS-<version>-<release>.fc44.src.rpm
  ```

- Prefer `copr-cli status <build-id>`, `copr-cli list-builds archjun/melonDS`, and COPR build logs to infer build state.
- If `copr-cli` returns an authentication/API response error, check `~/.config/copr` token expiration before changing packaging.

## Known Packaging Lessons

- `qt6-qtbase-private-devel` provides `qpa/qplatformnativeinterface.h` on Fedora 44.
- A missing `qpa/qplatformnativeinterface.h` error in the old `melonDS-1.0` build was not a missing `BuildRequires`; the package was installed. The upstream `melonDS-1.1` source changed the Qt private-header include path behavior for Qt >= 6.5 and is the correct fix.
- Keep `qt6-qtbase-private-devel` in `BuildRequires` while upstream uses Qt private headers.

## Verification

- For Makefile/spec metadata changes, run at least:

  ```sh
  make check-upstream-version
  make test
  rpmspec -q --srpm SPECS/melonDS.spec
  ```

- For COPR packaging changes, run `make srpm` and inspect the generated SRPM metadata with `rpm -qpi` before upload.
