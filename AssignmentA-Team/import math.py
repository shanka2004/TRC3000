import math

def generate_spiral_gcode(radius, step_size, feed_rate, offset_x, offset_y, count, z_max):
    gcode = []
    
    # Initialize G-code
    gcode.append("G21 ; Set units to millimeters")
    gcode.append("G90 ; Use absolute positioning")
    gcode.append(f"G1 F{feed_rate} ; Set feed rate")
    
    for loop in range(count):
        # Start at the new center for each loop
        gcode.append(f"G0 X{offset_x:.3f} Y{offset_y:.3f} Z0.000")
        # Inward spiral with decreasing Z-axis movement
        angle = 0
        r = 0
        while r <= radius:
            x = r * math.cos(math.radians(angle)) + offset_x
            y = r * math.sin(math.radians(angle)) + offset_y
            z = 0.00  # Gradually decrease Z as radius decreases
            gcode.append(f"G1 X{x:.3f} Y{y:.3f} Z{z:.3f}")
            
            angle += step_size
            r = angle * step_size / 360
        
        # Outward spiral with increasing Z-axis movement
        angle = 0
        r = radius
        while r >= 0:
            x = r * math.cos(math.radians(angle)) + offset_x
            y = r * math.sin(math.radians(angle)) + offset_y
            z = z_max - (r / radius) * z_max  # Gradually increase Z as radius increases
            gcode.append(f"G1 X{x:.3f} Y{y:.3f} Z{z:.3f}")
            
            angle += step_size
            r = radius - angle * step_size / 360
        
        # Return to the outer edge at the max Z height
        gcode.append(f"G1 X{x:.3f} Y{y:.3f} Z{z_max:.3f}")
        
        
        # Return to the center at Z=0 after each loop
        gcode.append(f"G1 X{offset_x:.3f} Y{offset_y:.3f} Z0.000")
    
    # End of program
    gcode.append("M30 ; Program end and rewind")
    
    return gcode

# Parameters
radius = 3  # Final radius
step_size = 0.5  # Step size for each increment in degrees
feed_rate = 3000  # Feed rate in mm/min
offset_x = 0  # X offset for the center
offset_y = 0  # Y offset for the center
count = 3  # Number of spiral loops
z_max = 5.0  # Maximum Z height at the outer edge of the spiral

# Generate G-code
gcode = generate_spiral_gcode(radius, step_size, feed_rate, offset_x, offset_y, count, z_max)

# Save to file
with open("spiral_gcode.gcode", "w") as f:
    for line in gcode:
        f.write(line + "\n")

print("G-code generated and saved to spiral_gcode.gcode")
