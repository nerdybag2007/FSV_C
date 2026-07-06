import customtkinter as ctk
import webbrowser
import subprocess
import shutil


# ----------------------------
# Appearance
# ----------------------------
ctk.set_appearance_mode("Dark")       # "Dark", "Light", or "System"
ctk.set_default_color_theme("blue")   # Theme color

# ----------------------------
# Main Window
# ----------------------------
app = ctk.CTk()
app.title("Mode Launcher")
app.geometry("500x400")
app.resizable(False, False)

# ----------------------------
# Title
# ----------------------------
title = ctk.CTkLabel(
    app,
    text="Welcome, Gursimar 👋",
    font=("Arial", 28, "bold")
)
title.pack(pady=30)

# ----------------------------
# Buttons
# ----------------------------


def coding_mode():
    brave = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

    subprocess.Popen([
        brave,
        "https://chatgpt.com",
        "https://claude.ai",
        "https://github.com",
        "https://leetcode.com",
        "https://www.hackerrank.com",
    ])


    import os
    os.system("code")
    
coding_btn = ctk.CTkButton(
    app,
    text="💻 Coding",
    width=250,
    height=50,
    command=coding_mode
)
coding_btn.pack(pady=10)

gaming_btn = ctk.CTkButton(
    app,
    text="🎮 Gaming",
    width=250,
    height=50
)
gaming_btn.pack(pady=10)

freedom_btn = ctk.CTkButton(
    app,
    text="🌴 Freedom",
    width=250,
    height=50
)
freedom_btn.pack(pady=10)

# ----------------------------
# Run the App
# ----------------------------
app.mainloop()