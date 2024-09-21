import tkinter as tk
from objects_management import ObjectManager


class NormalCursorApp(tk.Frame):
    def __init__(self, window_width, window_height, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry(f'{window_width}x{window_height}')  # Define window size
        self.canvas = tk.Canvas(self.master, bg='white', width=window_width, height=window_height)  # Create canvas
        self.canvas.pack()
        # Create and manage objects
        self.object_manager = ObjectManager(self.canvas)
        self.objects = self.object_manager.objects
        self.selected_object = None  # Tracking selected object
        # Binding left mouse click event to the on_object_click method to select an object
        self.canvas.bind("<Button-1>", self.on_object_click)

    def on_object_click(self, event):
        clicked_object = self.get_clicked_object(event.x, event.y)  # Check if an object was clicked after user clicks
        if clicked_object is not None:
            # Highlight the clicked object
            self.object_manager.highlight_object(clicked_object)
            self.selected_object = clicked_object  # Store the selected object index

    def get_clicked_object(self, x, y):
        # Iterate over objects to find the one clicked by the mouse
        for index, obj in enumerate(self.objects):
            # calculate Euclidean distance between the point clicked and the object center
            distance_to_object = ((x - obj['x']) ** 2 + (
                        y - obj['y']) ** 2) ** 0.5
            if distance_to_object <= obj['radius']:  # Check if click is within object's radius
                return index  # Return the index of the clicked object
        return None  # Return None if no object was clicked


if __name__ == '__main__':
    root = tk.Tk()
    app = NormalCursorApp(window_width=800, window_height=600, master=root)
    app.mainloop()
