# winload (Python edition)

## 📖 [👉 Click here for the full README 👈](../readme.md)

---

### 🇺🇸 Why does this file exist?

This is a **placeholder** `readme.md` for local development.

`pyproject.toml` declares `readme = "readme.md"`, so when you run `uv run` (or `pip install -e .`), the build backend **hatchling** performs an editable install and **validates that this file exists**. Without it, you get:

```
OSError: Readme file does not exist: readme.md
```

- **Local dev**: this placeholder keeps hatchling happy ✅
- **Github Acion CI → PyPI**: the workflow copies the root `readme.md` here before `uv build`, so PyPI always shows the full README ✅

---

### 🇨🇳 为什么需要这个文件？

这是一个用于本地开发的**占位** `readme.md`。

`pyproject.toml` 中声明了 `readme = "readme.md"`，当你执行 `uv run`（或 `pip install -e .`）时，构建后端 **hatchling** 会做 editable install 并**校验此文件是否存在**。如果没有，就会报错：

```
OSError: Readme file does not exist: readme.md
```

- **本地开发**：有这个占位文件，hatchling 校验就能通过 ✅
- **Github Acion CI → PyPI**：工作流会在 `uv build` 前将根目录的 `readme.md` 复制到此处，PyPI 页面始终显示完整 README ✅

## 📖 [👉 点击这里查看完整 README 👈](../readme.md)

---

### 🇹🇼 為什麼需要這個檔案？

這是一個用於本機開發的**佔位** `readme.md`。

`pyproject.toml` 中宣告了 `readme = "readme.md"`，當你執行 `uv run`（或 `pip install -e .`）時，建置後端 **hatchling** 會做 editable install 並**驗證此檔案是否存在**。如果沒有，就會報錯：

```
OSError: Readme file does not exist: readme.md
```

- **本機開發**：有這個佔位檔案，hatchling 驗證就能通過 ✅
- **Github Acion CI → PyPI**：工作流會在 `uv build` 前將根目錄的 `readme.md` 複製到此處，PyPI 頁面始終顯示完整 README ✅

## 📖 [👉 點擊這裡查看完整 README 👈](../readme.md)
