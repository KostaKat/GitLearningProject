import tkinter as tk

# Function to handle button click events
def on_button_click(input_char):
    if input_char == 'C':  # Clear the entry field
        entry.delete(0, tk.END)
    elif input_char == '=':  # Calculate the result
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(0, 'Error')
    else:  # Update the entry with the pressed button's text
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current + input_char)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the display area
entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button texts in a list
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Create and place buttons dynamically
for i, text in enumerate(button_texts):
    function = lambda x=text: on_button_click(x)
    button = tk.Button(root, text=text, padx=20, pady=20, command=function)
    row = (i // 4) + 1
    column = i % 4
    button.grid(row=row, column=column)

# Run the main event loop
root.mainloop()

