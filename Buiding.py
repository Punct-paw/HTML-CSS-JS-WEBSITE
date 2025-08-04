import tkinter as tk
import time

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = "#FFFFFF"
BLACK = "#000000"
BLUE = "#0000FF"

# Structure parameters
columns = 4
beams = 3
column_width = 20
beam_height = 20
spacing_x = WIDTH // (columns + 1)
spacing_y = HEIGHT // (beams + 1)
construction_speed = 500  # Milliseconds per element

# Lists to store structure elements
column_positions = []
beam_positions = []

# State variables
current_column = 0
current_beam = 0
construction_phase = "columns"  # Phases: columns, beams

# Set up the main window
root = tk.Tk()
root.title("Building Frame Construction")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=WHITE)
canvas.pack()

# Label for status
status_label = tk.Label(root, text="", font=("Arial", 12))
status_label.pack()

def setup():
    # Initialize column and beam positions
    for i in range(columns):
        column_positions.append((spacing_x * (i + 1), HEIGHT))
    for j in range(beams):
        for i in range(columns - 1):
            beam_positions.append((spacing_x * (i + 1), HEIGHT - spacing_y * (j + 1)))

def update_construction():
    global current_column, current_beam, construction_phase
    current_time = time.time()
    
    if construction_phase == "columns" and current_column < columns:
        x, y = column_positions[current_column]
        canvas.create_rectangle(
            x - column_width // 2, 0, x + column_width // 2, HEIGHT, fill=BLUE
        )
        current_column += 1
        if current_column == columns:
            construction_phase = "beams"
    elif construction_phase == "beams" and current_beam < len(beam_positions):
        x, y = beam_positions[current_beam]
        canvas.create_rectangle(
            x, y - beam_height // 2, x + spacing_x, y + beam_height // 2, fill=BLUE
        )
        current_beam += 1

    status = f"Phase: {construction_phase.capitalize()} | Progress: {min(current_column + current_beam, columns + len(beam_positions))}/{columns + len(beam_positions)}"
    status_label.config(text=status)

    if current_column + current_beam < columns + len(beam_positions):
        root.after(construction_speed, update_construction)


    # Update status
    status = f"Phase: {construction_phase.capitalize()} | Progress: {min(current_column + current_beam, columns + len(beam_positions))}/{columns + len(beam_positions)}"
    status_label.config(text=status)

    # Schedule next update
    if current_column + current_beam < columns + len(beam_positions):
        root.after(construction_speed, update_construction)

def main():
    setup()
    update_construction()
    root.mainloop()

if __name__ == "__main__":
    main()