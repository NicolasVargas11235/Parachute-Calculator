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


"""Main Script, Written by: Nicolas Vargas, Last Modified: 2023-10-28 by Jordan Trach"""
# Create the main window
root = tk.Tk()
root.title("Parachute Calculator")

# Create and place title header
header_frame = ttk.Frame(root)
header_frame['borderwidth'] = 5
header_frame['relief'] = 'raised'
header_frame['height'] = 20
header_frame.grid(column = 0, row = 0, columnspan = 15, sticky = (tk.E, tk.W))
label_header = tk.Label(header_frame, text = "Parachute Calculator", )
label_header.grid(column = 1, row = 0)

# Create and place sidebar for sought value
seeking_header = tk.Label(root, text = "Which value do you need?")
seeking_header.grid(column = 0, row = 1, columnspan = 2, padx = 5, pady = 5)

#Create and place value options (placeholders)
parachute_size_button = tk.Button(root, text = "Parachute Size", command=calculate_parachute)
parachute_size_button.grid(column = 0, row = 2, sticky = (tk.N, tk.S, tk.E, tk.W))

# Create and place main entry window for given values
given_frame = ttk.Frame(root)
given_frame['height'] = 20
given_frame.grid(column = 2, row = 1, columnspan = 3, sticky = (tk.E, tk.W))
given_header = tk.Label(root, text = "Enter known values:")
given_header.grid(column = 2, row = 1, columnspan = 5)

# Create and place given values table
entry_mass = tk.Entry(root)
entry_mass.grid(column = 2, row = 2, ipadx = 5, padx = 5)
label_mass = tk.Label(root, text="Load Mass (kg)")
label_mass.grid(column = 2, row = 3, ipadx = 5)

entry_velocity = tk.Entry(root)
entry_velocity.grid(column = 3, row = 2, ipadx = 5, padx = 5)
label_velocity = tk.Label(root, text="Descent Velocity (m/s)")
label_velocity.grid(column = 3, row = 3, ipadx = 5)

entry_drag_coefficient = tk.Entry(root)
entry_drag_coefficient.grid(column = 4, row = 2, ipadx = 5, padx = 5)
label_drag_coefficient = tk.Label(root, text="Drag Coefficient")
label_drag_coefficient.grid(column = 4, row = 3, ipadx = 5)

# Create and place sidebar for results
result_header = tk.Label(root, text = "Result")
result_header.grid(column = 5, row = 1, columnspan = 3, sticky = (tk.N, tk.S, tk.E, tk.W))
result_label = tk.Label(root)
result_label.grid(column = 5, row = 2)

# Start the GUI event loop
root.mainloop()
