import tkinter as tk
from tkinter import messagebox
import hashlib


def hash_password(password):
    """Возвращает SHA-256 хеш пароля."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


# Учебные учетные записи для демонстрации
USERS = {
    "admin": hash_password("1234"),
    "user": hash_password("qwerty"),
}

MAX_ATTEMPTS = 3
attempts_left = MAX_ATTEMPTS


def toggle_password():
    password_entry.config(show="" if show_password.get() else "*")


def check_login(event=None):
    global attempts_left

    login = login_entry.get().strip()
    password = password_entry.get()

    if not login or not password:
        messagebox.showwarning("Внимание", "Заполните все поля!")
        return

    if login in USERS and USERS[login] == hash_password(password):
        messagebox.showinfo("Успех", f"Добро пожаловать, {login}!")
        root.destroy()
        return

    attempts_left -= 1
    if attempts_left > 0:
        messagebox.showerror(
            "Ошибка",
            f"Неверный логин или пароль. Осталось попыток: {attempts_left}",
        )
        password_entry.delete(0, tk.END)
        password_entry.focus()
    else:
        messagebox.showerror(
            "Блокировка",
            "Попытки входа закончились. Приложение будет закрыто.",
        )
        root.destroy()


root = tk.Tk()
root.title("Авторизация")
root.geometry("360x330")
root.resizable(False, False)

tk.Label(
    root, text="Вход в систему", font=("Arial", 16, "bold")
).pack(pady=15)

tk.Label(root, text="Логин:").pack(anchor="w", padx=40)
login_entry = tk.Entry(root, width=30)
login_entry.pack(padx=40, pady=5)
login_entry.focus()

tk.Label(root, text="Пароль:").pack(anchor="w", padx=40)
password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack(padx=40, pady=5)

show_password = tk.BooleanVar(value=False)
tk.Checkbutton(
    root,
    text="Показать пароль",
    variable=show_password,
    command=toggle_password,
).pack(anchor="w", padx=40, pady=5)

tk.Button(
    root,
    text="Войти",
    width=15,
    command=check_login,
    bg="#4CAF50",
    fg="white",
    activebackground="#388E3C",
).pack(pady=18)

root.bind("<Return>", check_login)
root.mainloop()
