# 构建与发布工作流 (MIPS)

> **[📖 English](build_mips.md)**

## 📋 概述

MIPS 版本的 CI/CD 流水线完全由 **commit 信息中的关键词** 驱动。推送到 `main` 分支时，只需在 commit message 中包含对应关键词，GitHub Actions 会自动完成后续工作。

## 🔑 关键词

| Commit 信息中的关键词 | 构建 (MIPS EL + MIPS) | GitHub Release |
|----------------------|:---:|:---:|
| `build action` | ✅ | ❌ |
| `build release` | ✅ | ✅ |
| *(无关键词)* | ❌ | ❌ |

## 🚀 用法示例

```bash
# ============================================================
# 单个关键词
# ============================================================

# 仅构建，验证两个 MIPS 平台的编译
git commit --allow-empty -m "ci: test cross-compile (build action)"

# 构建 + 创建 GitHub Release
git commit -m "release: v0.2.0 (build release)"

# ============================================================
# 普通提交（不构建，不发布）
# ============================================================

# 仅更新文档
git commit -m "docs: update README"
# → 工作流将跳过所有任务
```

## ⚙️ 构建目标

| 目标 | 架构 | 说明 |
|------|------|------|
| `mipsel-unknown-linux-gnu` | MIPS EL（小端序） | 用于 MiWiFi Router 3G 等设备 |
| `mips-unknown-linux-gnu` | MIPS（大端序） | 用于旧款 MIPS 设备 |

## 📁 构建产物

成功构建后，可获取以下产物：

- `winload-mipsel-unknown-linux-gnu` — 小端序 MIPS 二进制文件
- `winload-mips-unknown-linux-gnu` — 大端序 MIPS 二进制文件

## 🔄 工作流阶段

```
推送到 main
    │
    ▼
┌─────────────────┐
│  check job      │  ← 解析 commit 信息，设置标志
└────────┬────────┘
         │ should_build?
         ▼
┌─────────────────┐
│  build job      │  ← 交叉编译两个 MIPS 目标
└────────┬────────┘
         │ should_release?
         ▼
┌─────────────────┐
│  release job    │  ← 创建 GitHub Release 并附上产物
└─────────────────┘
```
