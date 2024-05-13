import tkinter as tk

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("새로운 창")

    label = tk.Label(new_window, text="값 입력:")
    label.pack()

    entry = tk.Entry(new_window)
    entry.pack()

    def on_submit():
        value = entry.get()
        print("입력된 값:", value)
        new_window.destroy()

    submit_button = tk.Button(new_window, text="확인", command=on_submit)
    submit_button.pack()

root = tk.Tk()
root.title("주 창")

# 메인 창이 실행될 때 바로 새로운 창 열기
open_new_window()

root.mainloop()
