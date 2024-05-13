import tkinter as tk
import rulet

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Integer-String Input")
        
        self.int_values = []
        self.str_values = []
        self.open_new_window()
        # Frames
        self.input_frame = tk.Frame(self.master)
        self.input_frame.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.display_frame = tk.Frame(self.master)
        self.display_frame.pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Integer Entry
        self.int_label = tk.Label(self.input_frame, text="각 룰렛의 비율:")
        self.int_label.grid(row=0, column=0, pady=5)
        
        self.int_entry = tk.Entry(self.input_frame)
        self.int_entry.grid(row=1, column=0, pady=5)
        
        # String Entry
        self.str_label = tk.Label(self.input_frame, text="이름:")
        self.str_label.grid(row=2, column=0, pady=5)
        
        self.string_entry = tk.Entry(self.input_frame)
        self.string_entry.grid(row=3, column=0, pady=5)
        
        # Add Button
        self.add_button = tk.Button(self.input_frame, text="추가", command=self.add_to_list)
        self.add_button.grid(row=4, column=0, pady=5)
        
        # Display Button
        self.display_button = tk.Button(self.input_frame, text="출력", command=self.show_input)
        self.display_button.grid(row=5, column=0, pady=5)
        
        # Display Label
        self.display_label = tk.Label(self.display_frame, text="")
        self.display_label.pack()
        
        # # Open New Window Button
        # self.open_window_button = tk.Button(self.master, text="새 창 열기", command=self.open_new_window)
        # self.open_window_button.pack(pady=5)
        
    def add_to_list(self):
        int_text = self.int_entry.get()
        str_text = self.string_entry.get()
        self.display_label.config(text=f"룰렛의 비율: {int_text}\이름: {str_text}")
        if int_text:
            self.int_values.append(int_text)
        if str_text:
            self.str_values.append(str_text)
        
    def show_input(self):
        total = sum(map(float, self.int_values))
        if total != 100:
            self.display_label.config(text='룰렛의 각 칸의 비율이 너무 적거나, 너무 많습니다')
        else:
            int_text = ", ".join(self.int_values)
            str_text = ", ".join(self.str_values)
            self.display_label.config(text=f"룰렛의 비율: {int_text}\n이름들: {str_text}")
            rulet.create_roulette(self.int_values, self.str_values)
    
    def open_new_window(self):
        new_window = tk.Toplevel(self.master)
        new_window.title("새로운 창")

        label = tk.Label(new_window, text="값 입력:")
        label.pack()

        entry = tk.Entry(new_window)
        entry.pack()

        def on_submit():
            value = entry.get()
            print("입력된 값:", value)
            # 여기에 값을 따로 저장하는 코드 추가
            new_window.destroy()

        submit_button = tk.Button(new_window, text="확인", command=on_submit)
        submit_button.pack()

root = tk.Tk()
app = App(root)
root.mainloop()
