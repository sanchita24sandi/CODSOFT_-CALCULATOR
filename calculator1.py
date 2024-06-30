# Importing the tkinter library for GUI components
import tkinter as tk
# Importing the ttk module from tkinter for themed widgets
from tkinter import ttk

# Define the Calculator class, inheriting from tk.Tk, which is the main window object in Tkinter
class Calculator(tk.Tk):
    def __init__(self):
        # Initialize the Tkinter window
        super().__init__()
        self.title("Calculator")  # Set the window title
        self.geometry("400x600")  # Set the window size
        self.configure(bg="white")  # Set the background color to white
        
        self.expression = ""  # Initialize the expression to be evaluated
        
        self.create_widgets()  # Call the method to create and layout widgets

    def create_widgets(self):
        # Create the display entry widget where the expression/result will be shown
        self.display = ttk.Entry(self, font=("Arial", 24), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, sticky="nsew")
        
        # Define the buttons in the calculator
        button_texts = [
            '7', '8', '9', '/',  # First row
            '4', '5', '6', '*',  # Second row
            '1', '2', '3', '-',  # Third row
            '0', '.', '=', '+'   # Fourth row
        ]
        
        # Loop through the button texts and create corresponding buttons
        for i, text in enumerate(button_texts):
            # Create a button with a command to handle its click event
            button = ttk.Button(self, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=1 + i//4, column=i%4, ipadx=10, ipady=20, sticky="nsew")
        
        # Create a clear button to reset the display
        clear_button = ttk.Button(self, text="C", command=self.clear_display)
        clear_button.grid(row=5, column=0, columnspan=4, ipadx=10, ipady=20, sticky="nsew")
        
        # Configure the grid to make the layout responsive
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)  # Make rows resizable
            self.grid_columnconfigure(i % 4, weight=1)  # Make columns resizable
        
    def on_button_click(self, char):
        # Handle button clicks and update the expression
        if char == '=':
            self.calculate()  # Evaluate the expression when '=' is pressed
        else:
            self.expression += str(char)  # Append the character to the expression
            self.update_display()  # Update the display with the new expression
    
    def clear_display(self):
        # Clear the expression and update the display
        self.expression = ""  # Reset the expression
        self.update_display()  # Clear the display
    
    def update_display(self):
        # Update the display entry with the current expression
        self.display.delete(0, tk.END)  # Clear the display entry
        self.display.insert(tk.END, self.expression)  # Insert the new expression
    
    def calculate(self):
        # Evaluate the current expression and update the display with the result
        try:
            result = str(eval(self.expression))  # Evaluate the expression
            self.expression = result  # Update the expression with the result
        except Exception as e:
            self.expression = "Error"  # If there's an error, show "Error"
        self.update_display()  # Update the display with the result or error

# Main section to run the calculator application
if __name__ == "__main__":
    calculator = Calculator()  # Create an instance of the Calculator class
    calculator.mainloop()  # Run the main loop of the application
