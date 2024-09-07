def generate_back_and_forth_gcode(frequency, total_time, distance, feed_rate):
    gcode = []
    
    # Initialize G-code
    gcode.append("G21 ; Set units to millimeters")
    gcode.append("G91 ; Use relative positioning")  # Relative positioning mode

    
    # Calculate the number of cycles and the time per half-cycle
    cycles = int(frequency * total_time)
    time_per_half_cycle = 1 / (2 * frequency)
    
    # Calculate the feed rate needed to cover the distance in the given time per half-cycle
    half_cycle_feed_rate = distance / time_per_half_cycle
    gcode.append(f"G1 F{half_cycle_feed_rate} ; Set feed rate")
    for _ in range(cycles):
        # Move in the positive X direction
        gcode.append(f"G1 X{distance:.3f} F{half_cycle_feed_rate:.1f}")
        # Move back in the negative X direction
        gcode.append(f"G1 X{-distance:.3f} F{half_cycle_feed_rate:.1f}")
    
    # End of program
    gcode.append("M30 ; Program end and rewind")
    
    return gcode

# Parameters
frequency = 1.0  # Frequency in Hz (cycles per second)
total_time = 10  # Total time in seconds
distance = 10.0  # Distance to move in mm
feed_rate = 3000  # Feed rate in mm/min

# Generate G-code
gcode = generate_back_and_forth_gcode(frequency, total_time, distance, feed_rate)

# Save to file
with open("back_and_forth_gcode.gcode", "w") as f:
    for line in gcode:
        f.write(line + "\n")

print("G-code generated and saved to back_and_forth_gcode.gcode")
