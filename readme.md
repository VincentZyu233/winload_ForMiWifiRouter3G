![winload](https://socialify.git.ci/VincentZyu233/winload/image?custom_language=Rust&description=1&forks=1&issues=1&language=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F250448479%3Fs%3D200%26v%3D4&name=1&owner=1&pulls=1&stargazers=1&theme=Auto)

# Winload <img src="https://github.com/user-attachments/assets/62fec846-0442-47f6-bbba-78acdc8803ef" height="32px">

> A lightweight, real-time CLI tool for monitoring network bandwidth and traffic, inspired by Linux's nload.

> **[📖 English](readme.md)**
> **[📖 简体中文(大陆)](readme.zh-cn.md)**
> **[📖 繁體中文(台灣)](readme.zh-tw.md)**
> **[📖 日本語](readme.jp.md)**
> **[📖 한국어](readme.ko.md)**

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/VincentZyuApps/winload)
[![Gitee](https://img.shields.io/badge/Gitee-C71D23?style=for-the-badge&logo=gitee&logoColor=white)](https://gitee.com/vincent-zyu/winload)

[![Windows x64 | ARM64](https://img.shields.io/badge/Windows-x64_|_ARM64-0078D4?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/VincentZyuApps/winload/releases)
[![Linux x64 | ARM64](https://img.shields.io/badge/Linux-x64_|_ARM64-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://github.com/VincentZyuApps/winload/releases)
[![macOS x64 | ARM64](https://img.shields.io/badge/macOS-x64_|_ARM64-000000?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/VincentZyuApps/winload/releases)
[![Android x64 | ARM64](https://img.shields.io/badge/Android-x64_|_ARM64-3DDC84?style=for-the-badge&logo=android&logoColor=white)](https://github.com/VincentZyuApps/winload/releases)

[![PyPI](https://img.shields.io/badge/PyPI-3776AB?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/winload/)
[![npm](https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white)](https://www.npmjs.com/package/@vincentzyuapps/winload)
[![Crates.io](https://img.shields.io/badge/Crates.io-000000?style=for-the-badge&logo=rust&logoColor=white)](https://crates.io/crates/winload)

[![Scoop](https://img.shields.io/badge/Scoop-7B4AE2?style=for-the-badge&logo=scoop&logoColor=white)](https://scoop.sh/#/apps?q=%22https%3A%2F%2Fgithub.com%2FVincentZyuApps%2Fscoop-bucket%22&o=false)
[![AUR](https://img.shields.io/badge/AUR-1793D1?style=for-the-badge&logo=archlinux&logoColor=white)](https://aur.archlinux.org/packages/winload-rust-bin)
[![APT](https://img.shields.io/badge/APT-E95420?style=for-the-badge&logo=debian&logoColor=white)](https://github.com/VincentZyuApps/winload/releases)
[![RPM](https://img.shields.io/badge/RPM-CB1626?style=for-the-badge&logo=redhat&logoColor=white)](https://github.com/VincentZyuApps/winload/releases)

> **[📖 Build Docs](.github/workflows/build.md)**

## 🚀 Introduction
`Winload` brings an intuitive, visual network monitor to the modern terminal. It started as a Windows-focused tool to fill the `nload` gap, and now targets Linux and macOS as well.

## 🙏 Acknowledgements
Winload is inspired by the classic 「[nload](https://github.com/rolandriegel/nload)」 project by Roland Riegel. Many thanks for the original idea and experience.
https://github.com/rolandriegel/nload

## ✨ Key Features
- **Dual implementations**
	- **Rust edition**: fast, memory-safe, single static binary—great for everyday monitoring.
	- **Python edition**: easy to hack and extend for prototyping or integrations.
- **Cross-platform**: Windows, Linux, and macOS (x64 & ARM64).
- **Real-time visualization**: live incoming/outgoing graphs and throughput stats.
- **Minimal UI**: clean TUI that mirrors nload's ergonomics.

## 📊 Performance Benchmarks
> ⚡ Winload (Rust) achieves **~10ms startup** and **<5MB binary size**, significantly outperforming Python and matching C++ nload in efficiency.

![Winload Benchmark](docs/benchmark/benchmark.svg)

## 🐍 Python Edition Installation
> 💡 **Implementation Note**: Only PyPI and GitHub/Gitee provide Python edition.  
> Only Cargo provides Rust source code for local compilation.  
> All other package managers (Scoop, AUR, npm, APT, RPM) and GitHub Releases distribute **Rust binaries only**.
### Python (pip)
```bash
pip install winload
# recommend use uv:
# https://docs.astral.sh/uv/getting-started/installation/
# https://gitee.com/wangnov/uv-custom/releases
uv venv
uv pip install winload
uv run winload
uv run python -c "import shutil; print(shutil.which('winload'))"
```

## 📥 Rust Edition Installation (recommended)
### npm (cross-platform)
```bash
npm install -g @vincentzyuapps/winload
npm list -g @vincentzyuapps/winload
# on Windows, use win-nload to avoid conflict with System32\winload.exe
# on Linux/macOS, both winload and win-nload work
# or use npx directly
npx @vincentzyuapps/winload
```
> ⚠️ The old package `winload-rust-bin` has been deprecated. Please use `@vincentzyuapps/winload` instead. The scoped package name is required for [GitHub Packages](https://github.com/features/packages) compatibility.

> Includes 6 precompiled binaries for x86_64 & ARM64 across Windows, Linux, and macOS.

### Cargo (Build from source)
```bash
cargo install winload
cargo install --list
```
### Windows (Scoop)
```powershell
scoop bucket add vincentzyu https://github.com/VincentZyuApps/scoop-bucket
scoop install winload
# execute bin file
win-nload
Get-Command win-nload # Powershell
where win-nload # CMD
```
> 💡 Recommended: use [Windows Terminal](https://github.com/microsoft/terminal) instead of the legacy Windows Console for correct CJK character rendering and better TUI experience.
> ```powershell
> scoop bucket add versions
> scoop install windows-terminal-preview
> wtp
> ```

### Arch Linux (AUR):
```bash
paru -S winload-rust-bin
which winload
```

### Linux (one-liner)
> Supports Debian/Ubuntu and derivatives — Linux Mint, Pop!_OS, Deepin, UOS, etc. (apt)

> Supports Fedora/RHEL and derivatives — Rocky Linux, AlmaLinux, CentOS Stream, etc. (dnf)
```bash
curl -fsSL https://raw.githubusercontent.com/VincentZyuApps/winload/main/docs/install_scripts/install.sh | bash
which winload
```
> 📄 [View install script source](https://github.com/VincentZyuApps/winload/blob/main/docs/install_scripts/install.sh)

**🇨🇳 Gitee mirror (faster in China Mainland):**
```bash
curl -fsSL https://gitee.com/vincent-zyu/winload/raw/main/docs/install_scripts/install_gitee.sh | bash
which winload
```
> 📄 [View Gitee install script](https://gitee.com/vincent-zyu/winload/blob/main/docs/install_scripts/install_gitee.sh)

> ⚠️ These install scripts only support systems with **apt or dnf** package managers on **x86_64 / aarch64** architectures. For other platforms, use **npm** (`npm install -g @vincentzyuapps/winload`) or **Cargo** (`cargo install winload`) instead.

<details>
<summary>Manual install</summary>

**DEB (Debian/Ubuntu):**
```bash
# Download the latest .deb from GitHub Releases
sudo dpkg -i ./winload_*_amd64.deb
# or use apt (auto-resolves dependencies)
sudo apt install ./winload_*_amd64.deb
which winload
```

**RPM (Fedora/RHEL):**
```bash
sudo dnf install ./winload-*-1.x86_64.rpm
which winload
```

**Or download binaries directly from [GitHub Releases](https://github.com/VincentZyuApps/winload/releases).**

</details>

## ⌨️ Usage

```bash
winload              # Monitor all active network interfaces
winload -t 200       # Set refresh interval to 200ms
winload -d "Wi-Fi"   # Start with a specific device
winload -e           # Enable emoji decorations 🎉
winload --npcap      # Capture 127.0.0.1 loopback traffic (Windows, requires Npcap)
```

### Options

| Flag | Description | Default |
|------|-------------|---------|
| `-t`, `--interval <MS>` | Refresh interval in milliseconds | `500` |
| `-a`, `--average <SEC>` | Average calculation window in seconds | `300` |
| `-d`, `--device <NAME>` | Default device name (partial match) | — |
| `-e`, `--emoji` | Enable emoji decorations in TUI 🎉 | off |
| `-U`, `--unicode` | Use Unicode block characters for graph (█▓░·) | off |
| `-u`, `--unit <UNIT>` | Display unit: `bit` or `byte` | `bit` |
| `-b`, `--bar-style <STYLE>` | Bar style: `fill`, `color`, or `plain` | `fill` |
| `--in-color <HEX>` | Incoming graph color, hex RGB (e.g. `0x00d7ff`) | cyan |
| `--out-color <HEX>` | Outgoing graph color, hex RGB (e.g. `0xffaf00`) | gold |
| `-m`, `--max <VALUE>` | Fixed Y-axis max (e.g. `10M`, `1G`, `500K`) — *conflicts with `--smart-max`* | auto |
| `--smart-max [SECS]` | Smart adaptive Y-axis: auto-decays after traffic spikes (default half-life: 10s) — *conflicts with `--max`* | off |
| `-n`, `--no-graph` | Hide graph, show stats only | off |
| `--hide-separator` | Hide the separator line (row of equals signs) | off |
| `--no-color` | Disable all TUI colors (monochrome mode) | off |
| `--npcap` | **[Windows Rust Only]** Capture loopback traffic via Npcap (recommended) | off |
| `--debug-info` | Print network interface debug info and exit | — |
| `-h`, `--help` | Print help (`--help --emoji` for emoji version!) | — |
| `-V`, `--version` | Print version | — |

> **Y-axis scaling modes** — there are three mutually exclusive scenarios:
>
> | Mode | Flag | Behavior |
> |------|------|----------|
> | **Fixed max** | `--max <VALUE>` | Y-axis is locked to the specified value (e.g. `10M`, `1G`). |
> | **Smart max** | `--smart-max [SECS]` | Y-axis adapts automatically: jumps up on traffic spikes, then smoothly decays back down (exponential decay, default half-life 10 s). |
> | **History peak** | *(neither flag)* | Y-axis follows the historical maximum of each metric — the default behavior. |
>
> ⚠️ `--max` and `--smart-max` **conflict with each other** — you can only use one at a time.

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `←` / `→` or `↑` / `↓` | Switch network device |
| `F3` | Toggle debug info overlay (Minecraft-style) |
| `=` | Toggle separator line visibility |
| `c` | Toggle color on/off |
| `q` / `Esc` | Quit |

## 🪟 Windows Loopback (127.0.0.1)

Windows cannot report loopback traffic through standard APIs — this is a [functional deficiency in Windows' network stack](docs/win_loopback.md).

**To capture loopback traffic on Windows**, use the `--npcap` flag:

```bash
winload --npcap
```

This requires [Npcap](https://npcap.com/#download) installed with "Support loopback traffic capture" enabled during setup.

> I previously tried polling Windows' own `GetIfEntry` API directly, but the counters are always 0 for loopback — there is simply no NDIS driver behind the loopback pseudo-interface to count anything. That code path has been removed.

> 📖 For a deep dive into why Windows loopback is broken, see [docs/win_loopback.md](docs/win_loopback.md)

On Linux and macOS, loopback traffic works out of the box — no extra flags needed.

## 🖼️ Previews
#### Python Edition Preview
![docs/preview-py.png](docs/preview-py.png)

#### Rust Edition Preview
![docs/preview-rust.png](docs/preview-rust.png)

## 📦 Dependencies

### Python Edition

| Package | Version | Description |
|:---|:---|:---|
| [![psutil](https://img.shields.io/badge/psutil-≥7.0-FF6F00?style=flat-square&logo=python&logoColor=white)](https://github.com/giampaolo/psutil) | ≥7.0 | Process and system utilities |
| [![windows-curses](https://img.shields.io/badge/windows--curses-≥2.0-333333?style=flat-square&logo=python&logoColor=white)](https://github.com/zhirui2020/windows-curses) | ≥2.0 | Windows curses support |

### Rust Edition

| Package | Version | Description |
|:---|:---|:---|
| [![ratatui](https://img.shields.io/badge/ratatui-0.29-FF6F00?style=flat-square&logo=rust&logoColor=white)](https://github.com/ratatui-org/ratatui) | 0.29 | Terminal UI framework |
| [![crossterm](https://img.shields.io/badge/crossterm-0.28-333333?style=flat-square&logo=rust&logoColor=white)](https://github.com/crossterm-rs/crossterm) | 0.28 | Cross-platform terminal library |
| [![sysinfo](https://img.shields.io/badge/sysinfo-0.32-333333?style=flat-square&logo=rust&logoColor=white)](https://github.com/GuillaumeGomez/sysinfo) | 0.32 | System information library |
| [![clap](https://img.shields.io/badge/clap-4-FF6F00?style=flat-square&logo=rust&logoColor=white)](https://github.com/clap-rs/clap) | 4 | Command-line argument parser |
| [![pcap](https://img.shields.io/badge/pcap-2-333333?style=flat-square&logo=rust&logoColor=white)](https://github.com/pcap-parser/pcap) | 2 | Packet capture (optional, Windows) |
