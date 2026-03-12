import yt_dlp
import os
import time

# Palette Warna Cyberpunk
G = '\033[1;32m' # Hijau (Success)
Y = '\033[1;33m' # Kuning (Warning)
R = '\033[1;31m' # Merah (Error)
W = '\033[1;37m' # Putih (Text)
C = '\033[1;36m' # Cyan (Primary)
P = '\033[1;35m' # Ungu (Accent)
B = '\033[1;34m' # Biru (Deep)
N = '\033[0m'    # Reset Warna

def header():
    os.system('clear')
    print(f"{C}  __________________________________________________")
    print(f"{C} /                                                  \\")
    print(f"{C} |  {P}████████╗████████╗      ██████╗ ██╗     {C}         |")
    print(f"{C} |  {P}╚══██╔══╝╚══██╔══╝      ██╔══██╗██║     {C}         |")
    print(f"{C} |  {P}   ██║      ██║   █████╗██║  ██║██║     {C}         |")
    print(f"{C} |  {P}   ██║      ██║   ╚════╝██║  ██║██║     {C}         |")
    print(f"{C} |  {P}   ██║      ██║         ██████╔╝███████╗{C}         |")
    print(f"{C} |  {P}   ╚═╝      ╚═╝         ╚═════╝ ╚══════╝{C}         |")
    print(f"{C} |                                                  |")
    print(f"{C} |  {W}System: {G}Ready {C}│ {W}Tools: {Y}TT DL {C}│ {W}Dev: {P}zeroXploit {C}    |")
    print(f"{C} \__________________________________________________/{N}")

def menu():
    print(f"\n  {C}┌────────────────── {W}MAIN MENU {C}──────────────────┐")
    print(f"  {C}│                                            │")
    print(f"  {C}│  {C}[{W}01{C}] {W}Download Video {G}(Tanpa Watermark) {C}    │")
    print(f"  {C}│  {C}[{W}02{C}] {W}Download Audio {Y}(Format MP3)      {C}    │")
    print(f"  {C}│  {C}[{W}03{C}] {W}Update Engine  {P}(Versi Terbaru)   {C}    │")
    print(f"  {C}│  {C}[{W}00{C}] {R}Keluar Program                   {C}    │")
    print(f"  {C}│                                            │")
    print(f"  {C}└────────────────────────────────────────────┘")

def process_download(url, mode):
    print(f"\n  {C}[{Y}*{C}] {W}Menghubungkan ke database TikTok...")
    
    # Konfigurasi yt-dlp
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'outtmpl': '/sdcard/Download/%(title)s.%(ext)s',
    }

    if mode == '1':
        ydl_opts['format'] = 'best'
    else:
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"  {C}[{G}+{C}] {W}Metadata ditemukan! Sedang mengunduh...")
            ydl.download([url])
        
        print(f"\n  {G}SUCCESS! {W}File tersimpan di folder {Y}Download{N}")
    except Exception as e:
        print(f"\n  {R}[!] ERROR: {W}Pastikan link benar atau koneksi stabil!{N}")

if __name__ == "__main__":
    while True:
        header()
        menu()
        
        prompt = f"\n  {C}zero{P}Xploit{W}@{C}TT-DL {G}>> {W}"
        choice = input(prompt)

        if choice in ['1', '2']:
            link = input(f"  {C}[?] {W}Masukkan Link : {G}")
            if "tiktok" in link:
                process_download(link, choice)
                input(f"\n  {W}Tekan {Y}[Enter]{W} untuk kembali...")
            else:
                print(f"  {R}[!] Link tidak valid!")
                time.sleep(1.5)
                
        elif choice == '3':
            print(f"  {Y}[*] Memperbarui mesin TT-DL...")
            os.system("pip install -U yt-dlp")
            print(f"  {G}[+] Engine Berhasil Diupdate!")
            time.sleep(2)
            
        elif choice == '0' or choice == '00':
            print(f"\n  {P}[*] Terimakasih telah menggunakan TT-DL!{N}\n")
            break
        else:
            print(f"  {R}[!] Pilihan salah!")
            time.sleep(1)
