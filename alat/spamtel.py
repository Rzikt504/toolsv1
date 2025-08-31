import os, time, requests, random

# Warna terminal
W = '\033[0m'
G = '\033[92m'
R = '\033[91m'
Y = '\033[93m'
B = '\033[94m'
C = '\033[96m'

# Pilihan pesan acak
pesan_acak = [
    "🔥 Hacked by AnsXploit",
    "💣 SPAM MODE: VVIP ACTIVE",
    "🚀 Powered by Telegram API",
    "💥 Incoming spam...",
    "⚠️ Warning: Flooding target!",
    "💀 You've been detected!",
    "🔓 Open the gate!"
]

# Fungsi clear layar
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Tampilan kotak input
def box_input():
    clear()
    print(C + "┌" + "─" * 52 + "┐")
    print(C + "│" + Y + "             TELEGRAM SPAMMER VVIP              " + C + "│")
    print(C + "│" + G + "              Created by AnsXploit               " + C + "│")
    print(C + "├" + "─" * 52 + "┤")
    token  = input(C + "│" + W + " [🧾] Token Bot Telegram               : " + C)
    target = input(C + "│" + W + " [🎯] ID Target (User / Group)         : " + C)
    pesan  = input(C + "│" + W + " [💬] Pesan (kosong = random)          : " + C)
    print(C + "│" + Y + " [∞] SPAM TANPA BATAS. Tekan CTRL+C untuk stop     " + C + "│")
    print(C + "└" + "─" * 52 + "┘" + W)
    return token, target, pesan

# Tampilan log pengiriman
def tampilkan_log(log_lines):
    clear()
    print(C + "┌" + "─" * 52 + "┐")
    print(C + "│" + Y + "             🚀 SPAM SEDANG BERLANGSUNG...         " + C + "│")
    print(C + "├" + "─" * 52 + "┤")
    for line in log_lines[-10:]:
        print(C + "│ " + W + f"{line:<50}" + C + "│")
    print(C + "└" + "─" * 52 + "┘" + W)

# Main program
token, target, pesan = box_input()
pakai_random = (pesan.strip() == "")
log_lines = []
i = 1

try:
    while True:
        teks = pesan if not pakai_random else random.choice(pesan_acak)
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {"chat_id": target, "text": teks}
        r = requests.post(url, data=data)

        if r.status_code == 200:
            log_lines.append(f"[✔] Pesan ke-{i} terkirim")
        else:
            log_lines.append(f"[✖] Gagal di pesan ke-{i} (Cek ID/Token)")
            break

        tampilkan_log(log_lines)
        i += 1
        # Tanpa delay = spam secepat koneksi
        # time.sleep(0.01)  # opsional jika mau kasih delay
except KeyboardInterrupt:
    print(R + "\n[✖] SPAM dihentikan oleh pengguna.\n" + W)

print(G + f"\n[✓] Total pesan berhasil dikirim: {i - 1}\n" + W)