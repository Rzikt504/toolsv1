#hayo mau ngapain lu anak asu 🗿
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, time, subprocess
from dataclasses import dataclass
from typing import List

try:
    from pyfiglet import Figlet
except ImportError:
    Figlet = None

# Warna ANSI
RED    = "\033[31m"
GREEN  = "\033[32m"
BLUE   = "\033[34m"
WHITE  = "\033[97m"
CYAN   = "\033[36m"
YELLOW = "\033[33m"
MAG    = "\033[35m"
RESET  = "\033[0m"
BOLD   = "\033[1m"

COLORS_CYCLE = [RED, GREEN, BLUE]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_blink(duration: float = 1.5, fps: int = 18):
    frames = ["█", "▒"]
    total = int(duration * fps)
    for i in range(total):
        color = COLORS_CYCLE[i % len(COLORS_CYCLE)]
        char = frames[i % len(frames)]
        sys.stdout.write("\r " + color + char* (1 + (i % 8)) + RESET + "  Loading...")
        sys.stdout.flush()
        time.sleep(1.0 / fps)
    sys.stdout.write("\r" + " "*40 + "\r")
    sys.stdout.flush()

def figlet_title(text: str = "TOOLS V.01"):
    if Figlet is None:
        print(GREEN + BOLD + text + RESET)
        return
    f = Figlet(font='slant')
    print(GREEN + f.renderText(text) + RESET)

def hr(width: int = 60):
    print(CYAN + "═" * width + RESET)

def center(text: str, width: int) -> str:
    if len(text) >= width:
        return text[:width]
    pad = (width - len(text)) // 2
    return " " * pad + text + " " * (width - len(text) - pad)

@dataclass
class MenuItem:
    key: str
    label: str
    filepath: str  # path file Python

class FancyMenu:
    def __init__(self, title: str, items: List[MenuItem], width: int = 64):
        self.title = title
        self.items = items
        self.width = width

    def draw_box(self):
        w = self.width
        top    = MAG + "╔" + "═"* (w-2) + "╗" + RESET
        bottom = MAG + "╚" + "═"* (w-2) + "╝" + RESET
        print(top)
        print(MAG + "║" + RESET + BOLD + center(self.title, self.width-2) + RESET + MAG + "║" + RESET)
        print(MAG + "╠" + "═"* (self.width-2) + "╣" + RESET)
        for it in self.items:
            line = f"[{YELLOW}{it.key}{RESET}] {WHITE}{it.label}{RESET}"
            print(MAG + "║ " + RESET + line.ljust(self.width-3) + MAG + "║" + RESET)
        print(MAG + "╠" + "═"* (self.width-2) + "╣" + RESET)
        footer = "⚡ VVIP Tools Menu - Developer Rzikt ⚡"
        print(MAG + "║" + RESET + center(GREEN + footer + RESET, self.width-2) + MAG + "║" + RESET)
        print(bottom)

    def ask(self) -> str:
        print()
        return input(f"{BOLD}{GREEN}Pilih menu{RESET} {WHITE}[ketik nomor]{RESET}: ").strip().lower()

# Jalankan file Python di folder "alat"
def run_file(filepath: str):
    clear()
    figlet_title("TOOLS V.01")
    hr()
    print(GREEN + f"Menjalankan: {filepath}" + RESET)
    print()
    try:
        subprocess.run([sys.executable, filepath])
    except Exception as e:
        print(RED + f"Error: {e}" + RESET)
    print()
    input(GREEN + "Tekan Enter untuk kembali ke menu..." + RESET)

def exit_app():
    clear()
    print(GREEN + "Terima kasih sudah pakai TOOLS V.01 👋" + RESET)
    sys.exit(0)

def main():
    while True:
        clear()
        loading_blink(1.7)
        figlet_title("TOOLS V.01")
        hr()

        items = [
            MenuItem("1", "creat     = membuat sc deface", "alat/creat.py"),
            MenuItem("2", "darknet   = darknet",            "alat/darknet.py"),
            MenuItem("3", "ghosttrack= ghosttrack",        "alat/ghosttrack.py"),
            MenuItem("4", "mail      = brutemail",         "alat/mail.py"),
            MenuItem("5", "Spam pesan   = spam bot tele",      "alat/spamtel.py"),
            MenuItem("6", "defacer   = defacer",           "alat/defacer.py"),
            MenuItem("0", "Keluar",                        None),
        ]
        menu = FancyMenu(" ✨ MENU TOOLS V.01 ✨ ", items)
        menu.draw_box()

        choice = menu.ask()
        for it in items:
            if choice == it.key:
                if it.filepath:
                    run_file(it.filepath)
                else:
                    exit_app()
                break
        else:
            print(RED + "❌ Pilihan tidak valid!" + RESET)
            time.sleep(1.2)

if __name__ == "__main__":
    main()