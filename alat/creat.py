import os
import time
import sys
import random
from pyfiglet import Figlet

# ANSI color codes
COLORS = ['\033[31m', '\033[32m', '\033[34m', '\033[35m']  # Merah, Hijau, Biru, Ungu
RESET = '\033[0m'  # Reset warna

def clear_screen():
    """Membersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def colorful_loading_animation():
    """Menampilkan animasi loading warna-warni."""
    chars = "█▒"
    for i in range(40):
        color = random.choice(COLORS)
        time.sleep(0.05)
        sys.stdout.write('\r' + color + (chars[i % len(chars)] * (i // 2)) + RESET)
        sys.stdout.flush()
    print("\n")

def display_figlet(text, color='\033[34m'):  # Default warna biru
    """Menampilkan teks dengan gaya Figlet dengan warna."""
    f = Figlet(font='slant')
    print(color + f.renderText(text) + RESET)

def get_user_input():
    """Mengumpulkan input dari pengguna."""
    script_name = input("Masukkan nama script deface (contoh: index.html): ")
    background_type = input("Pilih background (warna/url): ").lower()
    if background_type == "warna":
        background = input("Masukkan warna background (contoh: black atau #000000): ")
        background_style = f"background-color: {background};"
    elif background_type == "url":
        background = input("Masukkan URL gambar background: ")
        background_style = f"background-image: url('{background}'); background-size: cover;"
    else:
        print("Pilihan tidak valid. Menggunakan background default (black).")
        background_style = "background-color: black;"

    deface_text = input("Masukkan kata-kata deface: ")
    icon_url = input("Masukkan URL ikon deface: ")

    mp3_choice = input("Pilih cara memasukkan URL MP3 (otomatis/atur/manual): ").lower()
    if mp3_choice == "otomatis":
        mp3_url = "URL_MP3_DEFAULT"  # Ganti dengan URL MP3 default Anda
    elif mp3_choice == "atur":
        mp3_url = input("Masukkan URL MP3: ")
    elif mp3_choice == "manual":
        mp3_url = "{MP3_URL}"  # Placeholder untuk input manual di HTML
    else:
        mp3_url = ""  # Tidak ada MP3

    return script_name, background_style, deface_text, icon_url, mp3_url

def create_deface_script(script_name, background_style, deface_text, icon_url, mp3_url):
    """Membuat script HTML deface."""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hacked!</title>
        <link rel="icon" href="{icon_url}">
        <style>
            body {{
                {background_style}
                color: white;
                font-family: monospace;
                text-align: center;
                padding-top: 100px;
            }}
        </style>
    </head>
    <body>
        <h1>You Have Been Hacked!</h1>
        <p>{deface_text}</p>
        <audio autoplay loop>
            <source src="{mp3_url}" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>
    </body>
    </html>
    """
    with open(script_name, "w") as f:
        f.write(html_content)
    print(f"Script deface berhasil dibuat: {script_name}")

def main():
    clear_screen()
    display_figlet("CREATER DEFACE", color='\033[34m')  # Warna biru
    colorful_loading_animation()

    script_name, background_style, deface_text, icon_url, mp3_url = get_user_input()
    create_deface_script(script_name, background_style, deface_text, icon_url, mp3_url)
    clear_screen()

if __name__ == "__main__":
    main()
