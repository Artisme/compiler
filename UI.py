import tkinter as tk
from tkinter import filedialog
import subprocess


def select_file():
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        input_file_text.configure(state="normal")
        input_file_text.delete(1.0, tk.END)
        with open(file_path, "r") as file:
            input_file_text.insert(tk.END, file.read())
            input_file_text.configure(state="disabled")

def run_program():
    if file_path:
        output_file_text.configure(state="normal")
        try:
            result = subprocess.run(
                ["python", "shell.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                input=f'RUN ("{file_path}")'.encode(),
            )
            print(result.stdout)
            stdout, stderr = result.stdout[8:], result.stderr
            if stdout:
                output_file_text.delete(1.0, tk.END)
                output_file_text.insert(tk.END, stdout.decode("utf-8"))
            if stderr:
                output_file_text.delete(1.0, tk.END)
                output_file_text.insert(tk.END, stderr.decode("utf-8"))
        except Exception as e:
            output_file_text.delete(1.0, tk.END)
            output_file_text.insert(tk.END, str(e))
        output_file_text.configure(state="disabled")

file_path = ""

root = tk.Tk()
root.resizable(False, False)
root.title("Basic Language Interpreter")

input_file_text = tk.Text(root, wrap=tk.WORD)
input_file_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
input_file_text.configure(state="disabled")

output_file_text = tk.Text(root, wrap=tk.WORD)
output_file_text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
output_file_text.configure(state="disabled")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=select_file)

run_button = tk.Button(root, text="RUN", command=run_program)
run_button.pack(side=tk.BOTTOM)

root.mainloop()
