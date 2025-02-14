import tkinter as tk
from tkinter import messagebox, Scrollbar
import random 

def calculate():
    try:
        alpha = float(alpha_entry.get())
        beta = float(beta_entry.get())
        n = float(n_entry.get())
        delta1 = float(delta1_entry.get())
        delta2 = float(delta2_entry.get())

        values = [round((alpha + (beta - alpha) * random.uniform(0, 1)), 2) for _ in range(20)]
        
        output_text = "Xi: " + ", ".join(map(str, values))
        
        output_text_box.delete(1.0, tk.END)  # Очистка предыдущего текста
        output_text_box.insert(tk.END, output_text)  # Вставка нового текста

        # Пример вычислений для Mx-m и Dx-g
        mx_m = round(sum(values) / len(values), 2)  # Пример Mx
        dx_g = round(sum((x - mx_m) ** 2 for x in values) / len(values), 2)  # Пример Dx

        mx_m_label.config(text=f"|Mx - m|: {mx_m}")
        dx_g_label.config(text=f"|Dx - g|: {dx_g}")

    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числа.")

def create_gui():
    global alpha_entry, beta_entry, n_entry, delta1_entry, delta2_entry, output_text_box
    global mx_m_label, dx_g_label

    root = tk.Tk()
    root.title("Вычисление значений")

    root.geometry("700x400")
    root.configure(bg="#2e2e2e")
    root.minsize(700, 400)
    frame = tk.Frame(root, padx=20, pady=20, bg="#3e3e3e")
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    title_label = tk.Label(frame, text="Генерация значений", font=("Helvetica", 18, "bold"), bg="#3e3e3e", fg="#ffffff")
    title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))

    # Первая строка с полями ввода a, b и N
    input_frame1 = tk.Frame(frame, bg="#3e3e3e")
    input_frame1.grid(row=1, column=0, sticky='ew', padx=5, pady=5)

    tk.Label(input_frame1, text='a:', bg="#3e3e3e", fg="#ffffff", font=("Helvetica", 12)).pack(anchor='w')
    alpha_entry = tk.Entry(input_frame1, font=("Helvetica", 12), bg="#ffffff", fg="#000000")
    alpha_entry.pack(fill=tk.X, padx=5, pady=5)

    input_frame2 = tk.Frame(frame, bg="#3e3e3e")
    input_frame2.grid(row=1, column=1, sticky='ew', padx=5, pady=5)

    tk.Label(input_frame2, text='b:', bg="#3e3e3e", fg="#ffffff", font=("Helvetica", 12)).pack(anchor='w')
    beta_entry = tk.Entry(input_frame2, font=("Helvetica", 12), bg="#ffffff", fg="#000000")
    beta_entry.pack(fill=tk.X, padx=5, pady=5)

    input_frame3 = tk.Frame(frame, bg="#3e3e3e")
    input_frame3.grid(row=1, column=2, sticky='ew', padx=5, pady=5)

    tk.Label(input_frame3, text='N:', bg="#3e3e3e", fg="#ffffff", font=("Helvetica", 12)).pack(anchor='w', pady=5)
    n_entry = tk.Entry(input_frame3, font=("Helvetica", 12), bg="#ffffff", fg="#000000")
    n_entry.pack(fill=tk.X, padx=5, pady=5)

    # Вторая строка для Mx-m и Dx-g
    mx_m_label = tk.Label(frame, text="", bg="#3e3e3e", fg="#ffffff", font=("Helvetica", 12))
    mx_m_label.grid(row=2, column=0, columnspan=3, sticky='ew', padx=5, pady=5)  # Это название для Mx-m

    dx_g_label = tk.Label(frame, text="", bg="#3e3e3e", fg="#ffffff", font=("Helvetica", 12))
    dx_g_label.grid(row=3, column=0, columnspan=3, sticky='ew', padx=5, pady=5)  # Это название для Dx-g

    # Кнопка вычисления
    calculate_button = tk.Button(frame, text='Подсчитать', command=calculate, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
    calculate_button.grid(row=4, column=0, columnspan=3, pady=15, sticky='ew')

    # Отделение области вывода
    separator = tk.Frame(frame, height=2, bd=1, relief="sunken", bg="#cccccc")
    separator.grid(row=5, column=0, columnspan=3, sticky='ew', pady=(10, 10))

    # Новый фрейм для вывода с темно-серыми оттенками
    output_frame = tk.Frame(frame, bg="#2e2e2e")
    output_frame.grid(row=6, column=0, columnspan=3, sticky='ew', padx=5, pady=5)

    # Создание виджета Text для вывода результатов
    output_text_box = tk.Text(output_frame, font=("Helvetica", 14), bg="#2e2e2e", fg="#ffffff", wrap=tk.WORD, padx=10, pady=10)
    output_text_box.pack(expand=True, fill=tk.BOTH)

    # Создание ползунка для прокрутки текста
    scrollbar = Scrollbar(output_frame, command=output_text_box.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    output_text_box.config(yscrollcommand=scrollbar.set)

    root.mainloop()

create_gui()
