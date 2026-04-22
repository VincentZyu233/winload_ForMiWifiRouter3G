# Build & Release Workflow (MIPS)

> **[📖 简体中文(大陆)](build_mips.zh-cn.md)**

## 📋 Overview

The CI/CD pipeline for MIPS builds is driven entirely by **commit message keywords**. Push to `main` with the right keyword and GitHub Actions takes care of the rest.

## 🔑 Keywords

| Keyword in commit message | Build (MIPS EL + MIPS) | GitHub Release |
|---------------------------|:---:|:---:|
| `build action` | ✅ | ❌ |
| `build release` | ✅ | ✅ |
| *(no keyword)* | ❌ | ❌ |

## 🚀 Usage Examples

```bash
# ============================================================
# Single keyword
# ============================================================

# Just build, verify compilation for both MIPS targets
git commit --allow-empty -m "ci: test cross-compile (build action)"

# Build + create GitHub Release
git commit -m "release: v0.2.0 (build release)"

# ============================================================
# Regular commits (no build, no publish)
# ============================================================

# Just update documentation
git commit -m "docs: update README"
# → Workflow will skip all jobs
```

## ⚙️ Build Targets

| Target | Architecture | Description |
|--------|--------------|-------------|
| `mipsel-unknown-linux-gnu` | MIPS EL (Little Endian) | For devices like MiWiFi Router 3G |
| `mips-unknown-linux-gnu` | MIPS (Big Endian) | For older MIPS devices |

## 📁 Artifacts

After a successful build, the following artifacts are available:

- `winload-mipsel-unknown-linux-gnu` — Little Endian MIPS binary
- `winload-mips-unknown-linux-gnu` — Big Endian MIPS binary

## 🔄 Workflow Stages

```
push to main
    │
    ▼
┌─────────────────┐
│  check job      │  ← Parse commit message, set flags
└────────┬────────┘
         │ should_build?
         ▼
┌─────────────────┐
│  build job      │  ← Cross-compile for both MIPS targets
└────────┬────────┘
         │ should_release?
         ▼
┌─────────────────┐
│  release job    │  ← Create GitHub Release with artifacts
└─────────────────┘
```
