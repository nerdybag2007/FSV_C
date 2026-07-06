import customtkinter as ctk

# Appearance
ctk.set_appearance_mode("Dark")      # Options: "Dark", "Light", "System"
ctk.set_default_color_theme("blue")  # Theme color

# Create window
app = ctk.CTk()
app.title("Mode Launcher")
app.geometry("500x400")

# Keep window running
app.mainloop()
title = ctk.CTkLabel(
    app,
    text="Welcome, Gursimar 👋",
    font=("Arial", 28, "bold")
)

title.pack(pady=30)