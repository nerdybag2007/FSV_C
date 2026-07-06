import os
import shutil
import subprocess
import webbrowser
import customtkinter as ctk

# ----------------------------
# Appearance & Window Config
# ----------------------------
ctk.set_appearance_mode("Dark")       # "Dark", "Light", or "System"
ctk.set_default_color_theme("blue")   # Theme color

app = ctk.CTk()
app.title("Mode Launcher")
app.geometry("450x450")
app.resizable(False, False)

# ----------------------------
# Mode Functions
# ----------------------------
def coding_mode():
    # Path to Brave browser
    brave = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
    
    # Check if Brave exists before trying to open it
    if os.path.exists(brave):
        subprocess.Popen([
            brave,
            "https://chatgpt.com",
            "https://claude.ai",
            "https://github.com",
            "https://leetcode.com",
            "https://www.hackerrank.com",
        ])
    else:
        # Fallback to default browser if Brave isn't found
        webbrowser.open("https://github.com")

    # Launch VS Code (using 'os.system' as per your original script)
    os.system("code")

def gaming_mode():
    print("Gaming Mode Activated! Add your launcher commands here.")
    # Example: subprocess.Popen([r"C:\Path\To\Steam.exe"])

def freedom_mode():
    print("Freedom Mode Activated! Add your chill/blocker commands here.")
    # Example: webbrowser.open("https://youtube.com")


# ----------------------------
# UI Elements
# ----------------------------

# Welcome Header
title_label = ctk.CTkLabel(
    app, 
    text="Welcome, Gursimar 👋", 
    font=ctk.CTkFont(family="Arial", size=26, weight="bold")
)
title_label.pack(pady=(40, 10))

# Subtitle
subtitle_label = ctk.CTkLabel(
    app, 
    text="Choose Your Session", 
    font=ctk.CTkFont(family="Arial", size=14),
    text_color="gray"
)
subtitle_label.pack(pady=(0, 25))

# --- Color Coding for Themes ---
coding_colors = ("#238636", "#2ea043")   # Tech/GitHub Green
gaming_colors = ("#8957e5", "#a371f7")   # Gaming Purple
freedom_colors = ("#f0883e", "#ff9e59")  # Relaxing Orange

# --- Custom Styling Arguments ---
button_style = {
    "master": app,
    "width": 260,
    "height": 55,
    "corner_radius": 25,  # Capsule look
    "font": ctk.CTkFont(family="Arial", size=16, weight="bold")
}

# --- Buttons ---
coding_btn = ctk.CTkButton(
    **button_style,
    text="💻   Coding Mode",
    fg_color=coding_colors[0],
    hover_color=coding_colors[1],
    command=coding_mode
)
coding_btn.pack(pady=12)

gaming_btn = ctk.CTkButton(
    **button_style,
    text="🎮   Gaming Mode",
    fg_color=gaming_colors[0],
    hover_color=gaming_colors[1],
    command=gaming_mode
)
gaming_btn.pack(pady=12)

freedom_btn = ctk.CTkButton(
    **button_style,
    text="🌴   Freedom Mode",
    fg_color=freedom_colors[0],
    hover_color=freedom_colors[1],
    command=freedom_mode
)
freedom_btn.pack(pady=12)

# ----------------------------
# Run the App
# ----------------------------
app.mainloop()