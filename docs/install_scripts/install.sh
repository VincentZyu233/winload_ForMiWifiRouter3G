#!/bin/bash
# winload installer — supports apt (deb) and dnf (rpm) on x86_64 / aarch64
# Usage: curl -fsSL https://raw.githubusercontent.com/VincentZyuApps/winload/main/docs/install_scripts/install.sh | bash
# Install specific version: WINLOAD_VERSION=v0.1.7-rc.10 bash -c "$(curl -fsSL https://...)"
set -e

REPO="VincentZyuApps/winload"
API_URL="https://api.github.com/repos/${REPO}/releases/latest"

# ── Detect architecture ──────────────────────────────────
ARCH=$(uname -m)
case "$ARCH" in
  x86_64|amd64)  ARCH_NAME="x86_64" ;;
  aarch64|arm64)  ARCH_NAME="aarch64" ;;
  *)
    echo "❌ Unsupported architecture: $ARCH"
    echo "   Only x86_64 and aarch64 are supported."
    echo ""
    echo "   Alternatives:"
    echo "   • npm (cross-platform): npx winload-rust-bin"
    echo "     https://www.npmjs.com/package/winload-rust-bin"
    echo "   • Manual download: https://github.com/${REPO}/releases"
    echo "   • Build from source: https://github.com/${REPO}"
    exit 1
    ;;
esac

# ── Detect package manager ───────────────────────────────
if command -v apt-get >/dev/null 2>&1; then
  PKG_MGR="apt"
elif command -v dnf >/dev/null 2>&1; then
  PKG_MGR="dnf"
else
  echo "❌ Unsupported package manager."
  echo "   This installer only supports apt (Debian/Ubuntu) and dnf (Fedora/RHEL)."
  echo "   Alternatives:"
  echo "   • npm (cross-platform): npx winload-rust-bin"
  echo "     https://www.npmjs.com/package/winload-rust-bin"
  echo "   • Manual download: https://github.com/${REPO}/releases"
  echo "   • Build from source: https://github.com/${REPO}"
  exit 1
fi

# ── Hint for Arch Linux users ────────────────────────────
if command -v pacman >/dev/null 2>&1; then
  echo ""
  echo "💡 Arch Linux detected! You can also install via AUR:"
  echo "   paru -S winload-rust-bin"
  echo "   https://aur.archlinux.org/packages/winload-rust-bin"
  echo ""
fi

echo "🔍 Detected: arch=$ARCH pkg_mgr=$PKG_MGR"

# ── Fetch release version ─────────────────────────────────
if [ -n "${WINLOAD_VERSION:-}" ]; then
  VERSION="$WINLOAD_VERSION"
  echo "📌 Using specified version: $VERSION"
else
  echo "📡 Fetching latest version..."
  VERSION=$(curl -fsSL "$API_URL" | grep '"tag_name"' | head -1 | sed 's/.*"tag_name": *"\([^"]*\)".*/\1/')
  if [ -z "$VERSION" ]; then
    echo "❌ Failed to fetch latest version from GitHub API."
    exit 1
  fi
  echo "📦 Latest version: $VERSION"
fi

# ── Download & Install ───────────────────────────────────
BASE_URL="https://github.com/${REPO}/releases/download/${VERSION}"
PLATFORM="linux-${ARCH_NAME}"
TMP_DIR=$(mktemp -d)
trap 'rm -rf "$TMP_DIR"' EXIT

if [ "$PKG_MGR" = "apt" ]; then
  PKG_FILE="winload-${PLATFORM}-${VERSION}.deb"
  echo "📥 Downloading ${PKG_FILE}..."
  curl -fSL -o "${TMP_DIR}/${PKG_FILE}" "${BASE_URL}/${PKG_FILE}"
  echo "📦 Installing via apt..."
  sudo dpkg -i "${TMP_DIR}/${PKG_FILE}" || sudo apt-get install -f -y
elif [ "$PKG_MGR" = "dnf" ]; then
  PKG_FILE="winload-${PLATFORM}-${VERSION}.rpm"
  echo "📥 Downloading ${PKG_FILE}..."
  curl -fSL -o "${TMP_DIR}/${PKG_FILE}" "${BASE_URL}/${PKG_FILE}"
  echo "📦 Installing via dnf..."
  sudo dnf install -y "${TMP_DIR}/${PKG_FILE}"
fi

echo ""
echo "✅ winload installed successfully!"
echo "   Run 'winload' to start monitoring."
echo ""
echo "   To uninstall:"
if [ "$PKG_MGR" = "apt" ]; then
  echo "   sudo apt remove winload"
elif [ "$PKG_MGR" = "dnf" ]; then
  echo "   sudo dnf remove winload"
fi
