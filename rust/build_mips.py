#!/usr/bin/env python3
"""
Cross-compile winload for OpenWrt / MIPS (MiWiFi Router 3G).

Required env vars:
    OPENWRT_SDK=/path/to/openwrt-sdk-23.05.4-ramips-mt7621_gcc-12.3.0_musl.Linux-x86_64

Usage:
    export OPENWRT_SDK=/root/mips-sdk/openwrt-sdk-23.05.4-ramips-mt7621_gcc-12.3.0_musl.Linux-x86_64
    python3 build_mips.py
"""

import os
import sys
from pathlib import Path


def main():
    # ─── 检查环境变量 ─────────────────────────────────────────────────
    sdk_path = os.environ.get("OPENWRT_SDK")
    if not sdk_path:
        print("❌ 错误: 未设置 OPENWRT_SDK 环境变量")
        print()
        print("请先设置环境变量:")
        print("  export OPENWRT_SDK=/root/mips-sdk/openwrt-sdk-23.05.4-ramips-mt7621_gcc-12.3.0_musl.Linux-x86_64")
        print()
        print("或者在命令行指定:")
        print("  OPENWRT_SDK=/root/mips-sdk/... python3 build_mips.py")
        sys.exit(1)

    SDK_BASE = Path(sdk_path).resolve()

    if not SDK_BASE.exists():
        print(f"❌ 错误: SDK 路径不存在: {SDK_BASE}")
        sys.exit(1)

    # 工具链路径
    TOOLCHAIN = SDK_BASE / "staging_dir" / "toolchain-mipsel_24kc_gcc-12.3.0_musl"
    TOOLCHAIN_BIN = TOOLCHAIN / "bin"
    SYSROOT = TOOLCHAIN

    # 检查GCC
    mipsel_gcc = TOOLCHAIN_BIN / "mipsel-openwrt-linux-gcc"
    if not mipsel_gcc.exists():
        print(f"❌ 错误: 交叉编译器不存在: {mipsel_gcc}")
        print("   SDK 可能未正确解压")
        sys.exit(1)

    # ─── 输出配置 ─────────────────────────────────────────────────────
    print("=" * 60)
    print("🔧 Cross-compile winload for OpenWrt MIPS")
    print("=" * 60)
    print(f"   SDK:       {SDK_BASE}")
    print(f"   GCC:       {mipsel_gcc}")
    print(f"   SYSROOT:   {SYSROOT}")
    print()

    # ─── 编译 ─────────────────────────────────────────────────────
    import subprocess

    # 环境变量
    env = os.environ.copy()
    env["PATH"] = f"{TOOLCHAIN_BIN}:{env.get('PATH', '')}"
    env["CARGO_TARGET_MIPSEL_UNKNOWN_LINUX_MUSL_LINKER"] = str(mipsel_gcc)
    env["CC"] = str(mipsel_gcc)
    env["CFLAGS"] = f"--sysroot={SYSROOT} -msoft-float -mips32r2 -O2"
    env["LDFLAGS"] = f"--sysroot={SYSROOT}"

    # 尝试编译
    MIPS_TARGET = "mipsel-unknown-linux-musl"

    cmd = [
        "cargo", "build",
        "--release",
        "--target", MIPS_TARGET,
    ]

    print(f"▶ {' '.join(cmd)}")
    print()

    result = subprocess.run(cmd, env=env)

    if result.returncode != 0:
        print()
        print("❌ 编译失败！")
        sys.exit(1)

    # ─── 后处理 ─────────────────────────────────────────────────────
    target_binary = Path("target") / MIPS_TARGET / "release" / "winload"
    if target_binary.exists():
        # strip
        strip_bin = TOOLCHAIN_BIN / "mipsel-openwrt-linux-strip"
        if strip_bin.exists():
            subprocess.run([str(strip_bin), str(target_binary)], check=False)

        # 验证
        file_info = subprocess.run(
            ["file", str(target_binary)],
            capture_output=True, text=True
        )

        size_kb = target_binary.stat().st_size // 1024

        print()
        print("=" * 60)
        print("🎉 编译成功！")
        print("=" * 60)
        print(f"   Binary: {target_binary}")
        print(f"   Size:   {size_kb} KB")
        if file_info.returncode == 0:
            print(f"   ELF:    {file_info.stdout.strip()}")
        print()
        print("📋 部署到路由器:")
        print(f"   scp {target_binary} root@192.168.5.1:/usr/bin/winload")
    else:
        print("❌ 编译产物未找到")
        sys.exit(1)


if __name__ == "__main__":
    main()
