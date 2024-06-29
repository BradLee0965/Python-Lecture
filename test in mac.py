import tkinter as tk
from tkinter import messagebox

class TesterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Modular Tester")

        # Initialize hardware connection status
        self.hardware_connected = False

        # Top label
        self.header = tk.Label(root, text="MODULAR TESTER", bg="#003f5c", fg="white", font=("Arial", 16))
        self.header.grid(row=0, columnspan=5, sticky="ew")

        # Buttons
        self.create_button("START", self.start_test, 1, 2)
        self.create_button("E-STOP", self.e_stop, 1, 3)
        self.create_button("STOP", self.stop_test, 1, 4)
        self.create_button("EXIT", self.exit_app, 1, 5)

        # Test item list (green box)
        self.test_list = tk.Listbox(root, bg="#90ee90", height=5)
        self.test_list.insert(1, "Pressure Proof Test")
        self.test_list.insert(2, "Leak Tester")
        self.test_list.insert(3, "Electrical Connectivity Test")
        self.test_list.grid(row=1, column=0, padx=10, pady=10)

        # Red indicators
        self.ereg_label = tk.Label(root, text="E-REG", bg="red", fg="white", width=15)
        self.ereg_label.grid(row=2, column=0, padx=5, pady=5)
        self.pressens_label = tk.Label(root, text="PRESSENS", bg="red", fg="white", width=15)
        self.pressens_label.grid(row=2, column=1, padx=5, pady=5)

        # Initialize hardware connection
        self.check_hardware_connection()

    def create_button(self, text, command, row, column):
        button = tk.Button(self.root, text=text, command=command, bg="#003f5c", fg="white", width=10)
        button.grid(row=row, column=column, padx=5, pady=5)

    def check_hardware_connection(self):
        # Simulate hardware connection check
        self.hardware_connected = True  # Simulating a successful hardware connection
        if self.hardware_connected:
            self.ereg_label.config(bg="green")
            self.pressens_label.config(bg="green")

    def start_test(self):
        selected_test = self.test_list.curselection()
        if selected_test:
            test_name = self.test_list.get(selected_test)
            messagebox.showinfo("Test Started", f"Starting {test_name}")
        else:
            messagebox.showwarning("No Test Selected", "Please select a test item from the list")

    def e_stop(self):
        messagebox.showinfo("E-STOP", "Emergency Stop Activated!")

    def stop_test(self):
        messagebox.showinfo("Stop", "Test Stopped")

    def exit_app(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = TesterGUI(root)
    root.mainloop()