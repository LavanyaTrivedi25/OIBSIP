import tkinter as tk
from tkinter import messagebox
import secrets
import string
import pyperclip

class PasswordGenerateor:
    def __init__(self, root):
        self.root = root
        self.root.title("Safe Password Generator")
        self.root.geometry("400x450")
        self.root.resizable(False, False)

        self.history = []
        
        tk.Label(root, text="Password Length (min 8):", font=("Arial", 10)).pack(pady=5)
        self.length_spin = tk.Spinbox(root, from_=8, to=32, width=5, font=("Arial", 10))
        self.length_spin.pack(pady=5)

        self.vari_upper = tk.BooleanVar(value=True)
        self.vari_lower = tk.BooleanVar(value=True)
        self.vari_nums = tk.BooleanVar(value=True)
        self.vari_syms = tk.BooleanVar(value=True)
        self.vari_ambig = tk.BooleanVar(value=False) 

        tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.vari_upper).pack(anchor="w", padx=50)
        tk.Checkbutton(root, text="Include Lowercase Letters", variable=self.vari_lower).pack(anchor="w", padx=50)
        tk.Checkbutton(root, text="Include Numbers", variable=self.vari_nums).pack(anchor="w", padx=50)
        tk.Checkbutton(root, text="Include Symbols", variable=self.vari_syms).pack(anchor="w", padx=50)
        tk.Checkbutton(root, text="Exclude Ambiguous (0, O, l, 1)", variable=self.vari_ambig).pack(anchor="w", padx=50)

        btn_generate = tk.Button(root, text="Generate Password", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=self.generate)
        btn_generate.pack(pady=15)

        self.lbl_result = tk.Label(root, text="", font=("Courier", 12, "bold"), fg="blue")
        self.lbl_result.pack(pady=5)

        self.lbl_strength = tk.Label(root, text="Strength: ---", font=("Arial", 10))
        self.lbl_strength.pack(pady=5)

        tk.Label(root, text="Recent Passwords (Last 5):", font=("Arial", 9, "italic")).pack(pady=5)
        self.lbl_history = tk.Label(root, text="", font=("Arial", 8), justify="left")
        self.lbl_history.pack(pady=5)

    def generate(self):
        try:
            length = int(self.length_spin.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid length!")
            return

        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        nums = string.digits
        syms = string.punctuation

        if self.vari_ambig.get():
            for char in "0Ol1":
                upper = upper.replace(char, "")
                lower = lower.replace(char, "")
                nums = nums.replace(char, "")
                syms = syms.replace(char, "")

        char_pools = []
        mandatory_chars = []

        if self.vari_upper.get():
            char_pools.append(upper)
            mandatory_chars.append(secrets.choice(upper))
        if self.vari_lower.get():
            char_pools.append(lower)
            mandatory_chars.append(secrets.choice(lower))
        if self.vari_nums.get():
            char_pools.append(nums)
            mandatory_chars.append(secrets.choice(nums))
        if self.vari_syms.get():
            char_pools.append(syms)
            mandatory_chars.append(secrets.choice(syms))

        if len(char_pools) < 2:
            messagebox.showwarning("Warning", "Please select at least 2 character types.")
            return

        if length < len(mandatory_chars):
            messagebox.showwarning("Warning", "Length is too short for selected character types.")
            return

        all_pool = "".join(char_pools)

        remaining_length = length - len(mandatory_chars)
        password_chars = mandatory_chars + [secrets.choice(all_pool) for _ in range(remaining_length)]
        
        password_list = list(password_chars)
        # Using secrets to shuffle securely
        for i in range(len(password_list) - 1, 0, -1):
            j = secrets.randbelow(i + 1)
            password_list[i], password_list[j] = password_list[j], password_list[i]
            
        password = "".join(password_list)

        self.lbl_result.config(text=password)
        pyperclip.copy(password)

        if length >= 12 and len(char_pools) >= 3:
            strength = "Strong"
            color = "green"
        elif length >= 10:
            strength = "Medium"
            color = "orange"
        else:
            strength = "Weak"
            color = "red"
        
        self.lbl_strength.config(text=f"Strength: {strength} (Copied to Clipboard!)", fg=color)

        if password not in self.history:
            self.history.append(password)
            if len(self.history) > 5:
                self.history.pop(0)
        self.lbl_history.config(text="\n".join(self.history))

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerateor(root)
    root.mainloop()