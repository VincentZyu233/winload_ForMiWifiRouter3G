"""
i18n.py - Internationalization support
Supported languages: en-us, zh-cn, zh-tw
"""

_current_lang = "en-us"

_STRINGS: dict[str, dict[str, str]] = {
    "en-us": {
        # ── CLI help ──
        "description": "Network Load Monitor — nload-like TUI tool for Windows/Linux/macOS",
        "help_interval": (
            "Refresh interval in milliseconds\n\n"
            "[default: 500]"
        ),
        "help_average": (
            "Average window in seconds\n\n"
            "[default: 300]"
        ),
        "help_device": "Default device name (partial match)",
        "help_emoji": "Enable emoji decorations in TUI 🎉",
        "help_unit": "Display unit: bit (default) or byte",
        "help_max": (
            "Fixed graph Y-axis max (e.g. 100M, 1G, 500K)\n\n"
            "[default: auto-scale]"
        ),
        "help_no_graph": "Hide traffic graphs, show only statistics",
        "help_unicode": "Use Unicode block characters for graph (█▓░· instead of #|..)",
        "help_bar_style": "Bar style: fill (default), color, plain",
        "help_in_color": (
            "Incoming (download) graph color, hex RGB (e.g. 0x00d7ff)\n\n"
            "[default: cyan]"
        ),
        "help_out_color": (
            "Outgoing (upload) graph color, hex RGB (e.g. 0xffaf00)\n\n"
            "[default: gold]"
        ),
        "help_hide_separator": "Hide separator line (the row of equals signs between header and panels)",
        "help_version": "Print version",
        "help_no_color": "Disable all TUI colors (monochrome mode), press 'c' to toggle at runtime",
        "help_smart_max": (
            "Smart adaptive Y-axis: auto-decays after traffic spikes\n\n"
            "[default half-life: 10s]"
        ),
        "help_debug_info": "Print debug info about network interfaces and exit",
        "help_lang": "Display language: en-us (default), zh-cn, zh-tw",
        # ── TUI strings ──
        "device": "Device",
        "device_emoji": "🖧 Device",
        "incoming": "Incoming",
        "incoming_emoji": "⬇️📥 Incoming",
        "outgoing": "Outgoing",
        "outgoing_emoji": "⬆️📤 Outgoing",
        "stat_curr": "Curr",
        "stat_avg": "Avg",
        "stat_min": "Min",
        "stat_max": "Max",
        "stat_ttl": "Ttl",
        "stat_curr_emoji": "⚡ Curr",
        "stat_avg_emoji": "📊  Avg",
        "stat_min_emoji": "📏  Min",
        "stat_max_emoji": "🚀  Max",
        "stat_ttl_emoji": "📦  Ttl",
        "help_bar": " ←/→ Switch Device | q Quit",
        "help_bar_emoji": " ⬅️/➡️ Switch Device | 🚪 q Quit",
        "terminal_too_small": "Terminal too small!",
        "terminal_too_small_emoji": "😭 Terminal too small! 📌",
        "loopback_warning": " ⚠ Loopback: stats may be inaccurate on Windows",
        # ── Error messages ──
        "error_no_curses": "Error: please install windows-curses first",
    },
    "zh-cn": {
        # ── CLI help ──
        "description": "网络负载监控工具 — 仿 Linux nload 的终端网络流量监控工具",
        "help_interval": (
            "刷新间隔（毫秒）\n\n"
            "[默认: 500]"
        ),
        "help_average": (
            "平均值计算窗口（秒）\n\n"
            "[默认: 300]"
        ),
        "help_device": "默认网卡名称（支持部分匹配）",
        "help_emoji": "启用 emoji 装饰模式 🎉",
        "help_unit": "显示单位：bit（默认）或 byte",
        "help_max": (
            "固定图形 Y 轴最大值（如 100M、1G、500K）\n\n"
            "[默认: 自动缩放]"
        ),
        "help_no_graph": "隐藏流量图形，仅显示统计信息",
        "help_unicode": "使用 Unicode 块字符绘制图形（█▓░· 代替 #|..）",
        "help_bar_style": "状态栏样式：fill（默认），color，plain",
        "help_in_color": (
            "入站（下载）图形颜色，十六进制 RGB（如 0x00d7ff）\n\n"
            "[默认: 青色]"
        ),
        "help_out_color": (
            "出站（上传）图形颜色，十六进制 RGB（如 0xffaf00）\n\n"
            "[默认: 金色]"
        ),
        "help_hide_separator": "隐藏分隔线（标题和面板之间的等号行）",
        "help_version": "打印版本号",
        "help_no_color": "禁用所有 TUI 颜色（单色模式），运行时按 c 可切换",
        "help_smart_max": (
            "智能自适应 Y 轴上限：流量尖峰后自动指数回落\n\n"
            "[默认半衰期: 10秒]"
        ),
        "help_debug_info": "打印网卡调试信息并退出",
        "help_lang": "显示语言：en-us（默认），zh-cn，zh-tw",
        # ── TUI strings ──
        "device": "设备",
        "device_emoji": "🖧 设备",
        "incoming": "入站",
        "incoming_emoji": "⬇️📥 入站",
        "outgoing": "出站",
        "outgoing_emoji": "⬆️📤 出站",
        "stat_curr": "当前",
        "stat_avg": "平均",
        "stat_min": "最小",
        "stat_max": "最大",
        "stat_ttl": "总计",
        "stat_curr_emoji": "⚡ 当前",
        "stat_avg_emoji": "📊 平均",
        "stat_min_emoji": "📏 最小",
        "stat_max_emoji": "🚀 最大",
        "stat_ttl_emoji": "📦 总计",
        "help_bar": " ←/→ 切换设备 | q 退出",
        "help_bar_emoji": " ⬅️/➡️ 切换设备 | 🚪 q 退出",
        "terminal_too_small": "终端窗口太小！",
        "terminal_too_small_emoji": "😭 终端窗口太小！📌",
        "loopback_warning": " ⚠ 回环设备：Windows 上统计可能不准确",
        # ── Error messages ──
        "error_no_curses": "错误：请先安装 windows-curses",
    },
    "zh-tw": {
        # ── CLI help ──
        "description": "網路負載監控工具 — 仿 Linux nload 的終端網路流量監控工具",
        "help_interval": (
            "重新整理間隔（毫秒）\n\n"
            "[預設: 500]"
        ),
        "help_average": (
            "平均值計算視窗（秒）\n\n"
            "[預設: 300]"
        ),
        "help_device": "預設網路卡名稱（支援部分匹配）",
        "help_emoji": "啟用 emoji 裝飾模式 🎉",
        "help_unit": "顯示單位：bit（預設）或 byte",
        "help_max": (
            "固定圖形 Y 軸最大值（如 100M、1G、500K）\n\n"
            "[預設: 自動縮放]"
        ),
        "help_no_graph": "隱藏流量圖形，僅顯示統計資訊",
        "help_unicode": "使用 Unicode 區塊字元繪製圖形（█▓░· 取代 #|..）",
        "help_bar_style": "狀態列樣式：fill（預設），color，plain",
        "help_in_color": (
            "入站（下載）圖形顏色，十六進位 RGB（如 0x00d7ff）\n\n"
            "[預設: 青色]"
        ),
        "help_out_color": (
            "出站（上傳）圖形顏色，十六進位 RGB（如 0xffaf00）\n\n"
            "[預設: 金色]"
        ),
        "help_hide_separator": "隱藏分隔線（標題和面板之間的等號行）",
        "help_version": "列印版本號",
        "help_no_color": "停用所有 TUI 顏色（單色模式），執行時按 c 可切換",
        "help_smart_max": (
            "智慧自適應 Y 軸上限：流量尖峰後自動指數回落\n\n"
            "[預設半衰期: 10秒]"
        ),
        "help_debug_info": "列印網路卡除錯資訊並退出",
        "help_lang": "顯示語言：en-us（預設），zh-cn，zh-tw",
        # ── TUI strings ──
        "device": "裝置",
        "device_emoji": "🖧 裝置",
        "incoming": "入站",
        "incoming_emoji": "⬇️📥 入站",
        "outgoing": "出站",
        "outgoing_emoji": "⬆️📤 出站",
        "stat_curr": "目前",
        "stat_avg": "平均",
        "stat_min": "最小",
        "stat_max": "最大",
        "stat_ttl": "總計",
        "stat_curr_emoji": "⚡ 目前",
        "stat_avg_emoji": "📊 平均",
        "stat_min_emoji": "📏 最小",
        "stat_max_emoji": "🚀 最大",
        "stat_ttl_emoji": "📦 總計",
        "help_bar": " ←/→ 切換裝置 | q 退出",
        "help_bar_emoji": " ⬅️/➡️ 切換裝置 | 🚪 q 退出",
        "terminal_too_small": "終端視窗太小！",
        "terminal_too_small_emoji": "😭 終端視窗太小！📌",
        "loopback_warning": " ⚠ 回環裝置：Windows 上統計可能不準確",
        # ── Error messages ──
        "error_no_curses": "錯誤：請先安裝 windows-curses",
    },
}


def set_lang(lang: str) -> None:
    """Set the current display language."""
    global _current_lang
    lang = lang.lower().strip()
    if lang in _STRINGS:
        _current_lang = lang
    else:
        _current_lang = "en-us"


def get_lang() -> str:
    """Get the current display language."""
    return _current_lang


def t(key: str) -> str:
    """Look up a translated string by key. Falls back to en-us, then to the key itself."""
    table = _STRINGS.get(_current_lang, _STRINGS["en-us"])
    result = table.get(key)
    if result is not None:
        return result
    # fallback to English
    result = _STRINGS["en-us"].get(key)
    if result is not None:
        return result
    return key
