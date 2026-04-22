# 构建 MIPS 工作流

> **[📖 English](build_mips.md)**
> **[📖 简体中文](build_mips.zh-cn.md)**

## 概述

通过 GitHub Actions 将 `winload` 交叉编译为 **MIPS 架构**（OpenWrt 路由器 / 嵌入式 Linux MIPS 设备）。执行与否完全由 commit 信息中的关键词控制。

## 关键词

| Commit 信息中的关键词 | 阶段一 — 校验 | 阶段二 — 构建 | 阶段三 — GitHub Release |
|----------------------|:---:|:---:|:---:|
| `build action`        | ✅  | ✅  | ❌ |
| `build release`       | ✅  | ✅  | ✅  |
| *(无关键词)*          | ✅  | ❌  | ❌ |

> 此工作流不支持 PR（MIPS 交叉编译依赖 Linux x64 runner，暂无单独的 PR 工作流计划）。

## 用法

```bash
# 仅阶段一（校验 commit 信息，不构建）
git commit --allow-empty -m "docs: update README"

# 阶段一 + 阶段二（仅构建，不发布 Release）
git commit --allow-empty -m "ci: 交叉编译 MIPS (build action)"

# 阶段一 + 阶段二 + 阶段三（构建 + 创建 GitHub Release）
git commit -m "release: v0.2.0 (build release)"
```

## 构建目标

| Target | 架构 | 说明 |
|--------|:---:|------|
| `mipsel-unknown-linux-gnu` | MIPS Little-Endian (MIPS III) | OpenWrt 主流（ar71xx、ramips 等） |

## 产物

运行成功后，Release 中包含：

```
winload-{version}-mipsel-unknown-linux-gnu
```

文件体积很小 —— LTO + strip 后二进制文件非常精简。
