#ZAARA 231P023
import tkinter as tk
from tkinter import messagebox
def on_submit():
    name = entry_name.get()
    age = entry_age.get()
    gender = var_gender.get()
    is_subscribed = var_subscribe.get()

    # Display the user inputs in a message box
    messagebox.showinfo("Submitted Information", f"Name: {name}\nAge: {age}\nGender: {gender}\nSubscribed: {is_subscribed}")

# Function to create a custom dialog
def custom_dialog():
    response = messagebox.askyesno("Custom Dialog", "Do you want to continue?")
    if response:
        messagebox.showinfo("Response", "You chose 'Yes'")
    else:
        messagebox.showinfo("Response", "You chose 'No'")

# Create the main window
root = tk.Tk()
root.title("Python GUI Example")
root.geometry("400x400")

# Label for name input
label_name = tk.Label(root, text="Name:")
label_name.pack(pady=5)

# Textbox for name input
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

# Label for age input
label_age = tk.Label(root, text="Age:")
label_age.pack(pady=5)

# Textbox for age input
entry_age = tk.Entry(root)
entry_age.pack(pady=5)

# Radio button for gender
label_gender = tk.Label(root, text="Gender:")
label_gender.pack(pady=5)
var_gender = tk.StringVar(value="Not selected")
radio_male = tk.Radiobutton(root, text="Male", variable=var_gender, value="Male")
radio_male.pack()
radio_female = tk.Radiobutton(root, text="Female", variable=var_gender, value="Female")
radio_female.pack()

# Checkbox for subscription
var_subscribe = tk.BooleanVar(value=False)
checkbox_subscribe = tk.Checkbutton(root, text="Subscribe to newsletter by zaara", variable=var_subscribe)
checkbox_subscribe.pack(pady=5)

# Submit button
button_submit = tk.Button(root, text="Submit", command=on_submit)
button_submit.pack(pady=20)

# Button to open custom dialog
button_dialog = tk.Button(root, text="Open Custom Dialog", command=custom_dialog)
button_dialog.pack(pady=10)

# Run the main event loop
root.mainloop()
