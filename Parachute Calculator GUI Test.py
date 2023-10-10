import tkinter as tk

# Constants
GRAVITY = 9.81
AIR_DENSITY = 1.204

def calculate_parachute():
    """Caclulates the projected area of the parachute (hemisphere shape), 
    given the drag coefficient, desired descent rate and the load mass.
    
    Written by: Nicolas Vargas
    Last Modified: 2023-10-07
    """
    
    # Get the values from the user's inputs
    try:
        mass = float(entry_mass.get())
        velocity = float(entry_velocity.get())
        drag_coefficient = float(entry_drag_coefficient.get())
    except ValueError:
        result_label.config(text="Please enter valid numbers")
        return

    # Calculate parachute size (assuming projected area is a complete disk)
    parachute_size = (mass * GRAVITY) / (drag_coefficient * AIR_DENSITY * velocity)
    
    # Update the result label
    result_label.config(text=f"Required Parachute Size: {parachute_size:.2f} square meters")


"""Main Script, Written by: Nicolas Vargas, Last Modified: 2023-10-10 by Jordan Trach"""
# Create the main window
root = tk.Tk()
root.title("Parachute Calculator")

#Create and place title header
label_header = tk.Label(root, text = "Parachute Calculator", bg = "white")
label_header.grid(column = 0, row = 0, columnspan = 10, sticky = (tk.N, tk.S, tk.E, tk.W))

# Create and place labels and respective entry widgets
label_mass = tk.Label(root, text="Enter Load Mass (kg):")
label_mass.grid(column = 1, row = 1, ipadx = 5)
entry_mass = tk.Entry(root)
entry_mass.grid(column = 2, row = 1, ipadx = 5)

label_velocity = tk.Label(root, text="Enter Descent Velocity (m/s):")
label_velocity.grid(column = 1, row = 2, ipadx = 5)
entry_velocity = tk.Entry(root)
entry_velocity.grid(column = 2, row = 2, ipadx = 5)

label_drag_coefficient = tk.Label(root, text="Enter Drag Coefficient:")
label_drag_coefficient.grid(column = 1, row = 3, ipadx = 5)
entry_drag_coefficient = tk.Entry(root)
entry_drag_coefficient.grid(column = 2, row = 3, ipadx = 5)

# Create and place a button to calculate
calculate_button = tk.Button(root, text="Calculate Parachute Size", command=calculate_parachute)
calculate_button.grid(column = 1, row = 4, ipadx = 5)

# Create and place a label to display the result
result_label = tk.Label(root, text="")
result_label.grid(column = 3, row = 1, rowspan = 3, ipadx = 5)

# Start the GUI event loop
root.mainloop()
