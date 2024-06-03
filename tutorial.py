"""Module Docstring"""

import ttkbootstrap as ttk

root = ttk.Window(themename="superhero")

# b1 = ttk.Button(root, text="primary", bootstyle="primary")
# b1.pack(side="left", padx=5, pady=5)

# b2 = ttk.Button(root, text="secondary", bootstyle="secondary")
# b2.pack(side="left", padx=5, pady=5)

# b3 = ttk.Button(root, text="success", bootstyle="success")
# b3.pack(side="left", padx=5, pady=5)

# b4 = ttk.Button(root, text="info", bootstyle="info")
# b4.pack(side="left", padx=5, pady=5)

# b5 = ttk.Button(root, text="warning", bootstyle="warning")
# b5.pack(side="left", padx=5, pady=5)

# b6 = ttk.Button(root, text="danger", bootstyle="danger")
# b6.pack(side="left", padx=5, pady=5)

# b7 = ttk.Button(root, text="light", bootstyle="light")
# b7.pack(side="left", padx=5, pady=5)

# b8 = ttk.Button(root, text="dark", bootstyle="dark")
# b8.pack(side="left", padx=5, pady=5)

for color in root.style.colors:
    b = ttk.Button(root, text=color, bootstyle=color)
    b.pack(side="left", padx=5, pady=5)

root.mainloop()
