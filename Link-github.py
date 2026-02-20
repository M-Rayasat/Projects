import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import re

class LinkGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GitHub Link Generator")
        self.root.geometry("500x500")

        self.dir_list = []

        # Configure styles
        style = ttk.Style()
        style.configure("TButton", padding=6)
        style.configure("TLabel", padding=6)

        # Main container
        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Username Input
        username_frame = ttk.Frame(main_frame)
        username_frame.pack(fill=tk.X, pady=(0, 10))

        ttk.Label(username_frame, text="GitHub Username:").pack(anchor=tk.W)
        self.username_var = tk.StringVar(value="M-Rayasat")
        self.username_entry = ttk.Entry(username_frame, textvariable=self.username_var)
        self.username_entry.pack(fill=tk.X, pady=(5, 0))

        # Directory Input
        dir_frame = ttk.Frame(main_frame)
        dir_frame.pack(fill=tk.X, pady=(0, 10))

        dir_input_frame = ttk.Frame(dir_frame)
        dir_input_frame.pack(fill=tk.X)

        ttk.Label(dir_input_frame, text="Directory/Repository:").pack(anchor=tk.W)
        self.dir_input = ttk.Entry(dir_input_frame)
        self.dir_input.pack(fill=tk.X, pady=(5, 5))
        self.dir_input.bind('<Return>', lambda event: self.add_directory())

        add_btn = ttk.Button(dir_frame, text="Add Component", command=self.add_directory)
        add_btn.pack(pady=(0, 10))

        # Directory List
        list_frame = ttk.Frame(main_frame)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        ttk.Label(list_frame, text="Path Components:").pack(anchor=tk.W)

        # Create listbox with scrollbar
        listbox_container = ttk.Frame(list_frame)
        listbox_container.pack(fill=tk.BOTH, expand=True, pady=(5, 5))

        self.listbox = tk.Listbox(listbox_container)
        scrollbar = ttk.Scrollbar(listbox_container, orient="vertical", command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=scrollbar.set)

        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        btn_frame = ttk.Frame(list_frame)
        btn_frame.pack(fill=tk.X)
        ttk.Button(btn_frame, text="Remove Selected", command=self.remove_selected).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(btn_frame, text="Clear All", command=self.clear_all).pack(side=tk.LEFT)
        ttk.Button(btn_frame, text="Move Up", command=self.move_up).pack(side=tk.RIGHT, padx=(5, 0))
        ttk.Button(btn_frame, text="Move Down", command=self.move_down).pack(side=tk.RIGHT)

        # Generate Section
        gen_frame = ttk.Frame(main_frame)
        gen_frame.pack(fill=tk.X)

        ttk.Button(gen_frame, text="Generate & Copy Link", command=self.generate_link).pack(fill=tk.X, pady=(0, 5))

        result_container = ttk.Frame(gen_frame)
        result_container.pack(fill=tk.X)

        ttk.Label(result_container, text="Generated Link:").pack(anchor=tk.W)
        self.result_link = tk.StringVar()
        self.result_entry = ttk.Entry(result_container, textvariable=self.result_link, state="readonly")
        self.result_entry.pack(fill=tk.X, pady=(5, 0))

        # Button to open link in browser
        open_btn_frame = ttk.Frame(gen_frame)
        open_btn_frame.pack(fill=tk.X, pady=(5, 0))
        ttk.Button(open_btn_frame, text="Open Link in Browser", command=self.open_link).pack(fill=tk.X)

    def add_directory(self):
        val = self.dir_input.get().strip()
        if val:
            # Validate directory name to ensure it's a valid GitHub Pages path component
            if self.is_valid_path_component(val):
                self.dir_list.append(val)
                self.listbox.insert(tk.END, val)
                self.dir_input.delete(0, tk.END)
            else:
                messagebox.showwarning("Invalid Input",
                    f"'{val}' is not a valid path component.\nUse letters, numbers, hyphens, underscores, and periods only.")

    def is_valid_path_component(self, component):
        """Validate that the path component is safe and follows GitHub Pages naming conventions."""
        # Allow alphanumeric, hyphens, underscores, and periods
        pattern = r'^[a-zA-Z0-9._-]+$'
        return bool(re.match(pattern, component)) and len(component) > 0

    def remove_selected(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            self.listbox.delete(index)
            self.dir_list.pop(index)

    def move_up(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            if index > 0:  # Can only move up if not at the top
                # Swap items in list
                item = self.dir_list.pop(index)
                self.dir_list.insert(index - 1, item)

                # Update listbox
                self.refresh_listbox()
                self.listbox.selection_set(index - 1)

    def move_down(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            if index < len(self.dir_list) - 1:  # Can only move down if not at the bottom
                # Swap items in list
                item = self.dir_list.pop(index)
                self.dir_list.insert(index + 1, item)

                # Update listbox
                self.refresh_listbox()
                self.listbox.selection_set(index + 1)

    def refresh_listbox(self):
        """Refresh the listbox to reflect the current order of items."""
        self.listbox.delete(0, tk.END)
        for item in self.dir_list:
            self.listbox.insert(tk.END, item)

    def clear_all(self):
        self.dir_list.clear()
        self.listbox.delete(0, tk.END)
        self.result_link.set("")

    def generate_link(self):
        username = self.username_var.get().strip()
        if not username:
            messagebox.showerror("Error", "Username cannot be empty")
            return

        # Validate username format
        if not self.is_valid_path_component(username):
            messagebox.showerror("Error", "Username contains invalid characters")
            return

        repo = "/".join(self.dir_list)
        if repo:
            link = f"https://{username}.github.io/{repo}"
        else:
            # If no path components, just use the base GitHub Pages URL
            link = f"https://{username}.github.io/"

        self.result_link.set(link)
        self.root.clipboard_clear()
        self.root.clipboard_append(link)
        messagebox.showinfo("Success", f"Link copied to clipboard:\n{link}")

    def open_link(self):
        link = self.result_link.get()
        if link:
            try:
                webbrowser.open(link)
            except Exception as e:
                messagebox.showerror("Error", f"Could not open link in browser:\n{str(e)}")
        else:
            messagebox.showwarning("No Link", "Please generate a link first")

if __name__ == "__main__":
    root = tk.Tk()
    app = LinkGeneratorApp(root)
    root.mainloop()