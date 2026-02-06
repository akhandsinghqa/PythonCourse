from pynput import mouse

# Variables to store our coordinates
start_pos = None
end_pos = None


def on_click(x, y, button, pressed):
    global start_pos, end_pos

    if button == mouse.Button.left:
        if pressed:
            # Step 1: Record the starting click
            start_pos = (x, y)
            print(f"Start Position: {start_pos}")
        else:
            # Step 2: Record the release point
            end_pos = (x, y)
            print(f"End Position: {end_pos}")

            # Stop the listener so we can perform the action
            return False


print("INSTRUCTIONS:")
print("1. Click and hold at the start of the text.")
print("2. Drag to the end of the text and release.")

# Start listening for the drag event
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
