from tkinter import *
from math import *

# Constants
GRAVITY = 9.81
AIR_DENSITY = 1.204
hf = 'Terminal'
bf = 'Fixedsys'
bkgc = 'gray11'
tbc = 'gray11'
tc = 'palegreen2'

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
    parachute_size = 2*(mass * GRAVITY) / (drag_coefficient * AIR_DENSITY * (velocity**2))
    
    # Update the result label
    result_label.config(text=f"Required Parachute Size: {parachute_size:.2f} square meters")

"""Equations for Stencil Calculation"""
def calculate_radius(area):
    radius = (area/pi)**0.5
    return radius


def calculate_stencil_base_size(area):
    """Calculates the base of stencil assuming that it 
    equals one eighth of circumference of the parachute skirt.
    
    Written by: Frank Ngo
    Last Modified: 2023-10-30
    """    
    
    
    radius = calculate_radius (area)
    base_size = float
    base_size = pi*(radius)/(4)
    return base_size

def calculate_stencil_height_size(area):
    """Calculates the height of stencil assuming that it is 2.25*(base_size). 
    Multiplier of 2.25 comes from ratios of the base size with respect to 
    radius"
    
    Written by: Frank Ngo
    Last Modified: 2023-10-30
    """   
   
   
    radius = calculate_radius (area)
    base_height = float
    base_height = 9*pi*(radius)/(16)
    return base_height

"""Arbitary area"""
area = 5 
print ("The stensil base size should be: " + str(calculate_stencil_base_size(area)))
print ("The stencil height size should be: " + str(calculate_stencil_height_size(area)))

# Create the main window
root = Tk()
root.title("Parachute Calculator")
root.configure(background = bkgc)

# Create and place title header
header = Label(root, text = "Parachute Stencil Generator", bg = tbc, fg = tc, font=(hf, 14), borderwidth = 1, relief = 'groove').grid(column = 0, row = 0, columnspan = 10, sticky = ('N','S','E','W'))


# Create and place sidebar for sought value
seeking_header = Label(root, text = "Which value do you need?", font=(bf, 12), bg = bkgc, fg = tc, padx = 10)
seeking_header.grid(column = 0, row = 1, columnspan = 2, padx = 5, pady = 5)

#Create and place value options (placeholders)
parachute_size_button = Button(root, text = "Parachute Size", font=(bf, 12), bg = tbc, fg = tc, command=calculate_parachute)
parachute_size_button.grid(column = 0, row = 2, sticky = (E, W))

# Create and place main entry window for given values
given_header = Label(root, text = "Enter known values:", font=(bf, 12), bg = bkgc, fg = tc)
given_header.grid(column = 2, row = 1, columnspan = 5)

# Create and place given values table
entry_mass = Entry(root, font=(bf, 12), bg = tbc, fg = tc)
entry_mass.grid(column = 2, row = 2, ipadx = 5, padx = 5)
label_mass = Label(root, text="Load Mass (kg)", font=(bf, 12), bg = tbc, fg = tc)
label_mass.grid(column = 2, row = 3, ipadx = 5)

entry_velocity = Entry(root, font=(bf, 12), bg = tbc, fg = tc)
entry_velocity.grid(column = 3, row = 2, ipadx = 5, padx = 5)
label_velocity = Label(root, text="Descent Velocity (m/s)", font=(bf, 12), bg = tbc, fg = tc)
label_velocity.grid(column = 3, row = 3, ipadx = 5)

entry_drag_coefficient = Entry(root, font=(bf, 12), bg = tbc, fg = tc)
entry_drag_coefficient.grid(column = 4, row = 2, ipadx = 5, padx = 5)
label_drag_coefficient = Label(root, text="Drag Coefficient", font=(bf, 12), bg = tbc, fg = tc)
label_drag_coefficient.grid(column = 4, row = 3, ipadx = 5)

# Create and place sidebar for results
result_header = Label(root, text = "Result", font=(bf, 12), bg = tbc, fg = tc)
result_header.grid(column = 5, row = 1, columnspan = 3)
result_label = Label(root, font=(bf, 12), bg = tbc, fg = tc)
result_label.grid(column = 5, row = 2)

# Start the GUI event loop
root.mainloop()
