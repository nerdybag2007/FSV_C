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
    
import customtkinter as ctk

app = ctk.CTk()
app.geometry("400x400")
app.title("Mode Selector")

# App Title
main_title = ctk.CTkLabel(
    app, 
    text="Choose Your Session", 
    font=ctk.CTkFont(size=22, weight="bold")
)
main_title.pack(pady=(40, 20))

# --- Color Coding for Themes ---
# Format: (normal_color, hover_color)
coding_colors = ("#238636", "#2ea043")   # Tech/GitHub Green
gaming_colors = ("#8957e5", "#a371f7")   # Gaming Purple
freedom_colors = ("#f0883e", "#ff9e59")  # Relaxing Orange

# --- Buttons ---
coding_btn = ctk.CTkButton(
    app,
    text="💻  Coding Mode",
    width=260,
    height=55,
    corner_radius=25,  # Capsule look
    font=ctk.CTkFont(size=16, weight="bold"),
    fg_color=coding_colors[0],
    hover_color=coding_colors[1],
    command=coding_mode
)
coding_btn.pack(pady=12)

gaming_btn = ctk.CTkButton(
    app,
    text="🎮  Gaming Mode",
    width=260,
    height=55,
    corner_radius=25,
    font=ctk.CTkFont(size=16, weight="bold"),
    fg_color=gaming_colors[0],
    hover_color=gaming_colors[1],
    command=gaming_mode
)
gaming_btn.pack(pady=12)

freedom_btn = ctk.CTkButton(
    app,
    text="🌴  Freedom Mode",
    width=260,
    height=55,
    corner_radius=25,
    font=ctk.CTkFont(size=16, weight="bold"),
    fg_color=freedom_colors[0],
    hover_color=freedom_colors[1],
    command=freedom_mode
)
freedom_btn.pack(pady=12)


# ----------------------------
# Run the App
# ----------------------------
app.mainloop()