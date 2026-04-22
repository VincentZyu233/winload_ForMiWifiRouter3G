# Build MIPS Workflow

> **[📖 English](build_mips.md)**
> **[📖 简体中文](build_mips.zh-cn.md)**

## Overview

Cross-compiles `winload` for **MIPS architecture** (OpenWrt routers / embedded Linux MIPS devices) via GitHub Actions. Execution is controlled entirely by commit message keywords.

## Keywords

| Keyword in commit message | Stage 1 — Check | Stage 2 — Build | Stage 3 — GitHub Release |
|---------------------------|:---:|:---:|:---:|
| `build action`            | ✅  | ✅  | ❌ |
| `build release`           | ✅  | ✅  | ✅  |
| *(none)*                  | ✅  | ❌  | ❌ |

> PRs are not supported by this workflow (MIPS cross-compilation requires a Linux x64 runner; a separate PR workflow is not planned for now).

## Usage

```bash
# Stage 1 only (commit message check, no build)
git commit --allow-empty -m "docs: update README"

# Stages 1 + 2 (build only, no release)
git commit --allow-empty -m "ci: cross-compile for MIPS (build action)"

# Stages 1 + 2 + 3 (build + create GitHub Release)
git commit -m "release: v0.2.0 (build release)"
```

## Build Targets

| Target | Architecture | Description |
|--------|:---:|------------|
| `mipsel-unknown-linux-gnu` | MIPS Little-Endian (MIPS III) | OpenWrt mainstream (ar71xx, ramips, etc.) |

## Artifacts

After a successful run, the release contains:

```
winload-{version}-mipsel-unknown-linux-gnu
```

Upload size is small — LTO + strip produces a minimal binary.
