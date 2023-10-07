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


"""Main Script, Written by: Nicolas Vargas, Last Modified: 2023-10-07"""
# Create the main window
root = tk.Tk()
root.title("Parachute Calculator")

# Create and place labels and respective entry widgets
label_mass = tk.Label(root, text="Enter Load Mass (kg):")
label_mass.pack()
entry_mass = tk.Entry(root)
entry_mass.pack()

label_velocity = tk.Label(root, text="Enter Descent Velocity (m/s):")
label_velocity.pack()
entry_velocity = tk.Entry(root)
entry_velocity.pack()

label_drag_coefficient = tk.Label(root, text="Enter Drag Coefficient:")
label_drag_coefficient.pack()
entry_drag_coefficient = tk.Entry(root)
entry_drag_coefficient.pack()

# Create and place a button to calculate
calculate_button = tk.Button(root, text="Calculate Parachute Size", command=calculate_parachute)
calculate_button.pack()

# Create and place a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI event loop
root.mainloop()
