import random


class ObjectManager:
    def __init__(self, canvas):
        self.canvas = canvas
        self.objects = self.create_objects()  # Create and store the objects

    def create_objects(self):
        start_button = {'x': 50, 'y': 550, 'radius': 20, 'color': 'blue'}
        target = {'x': 562, 'y': 50, 'radius': 20, 'color': 'red'}
        distractors = []
        for i in range(20):
            x, y = random.randint(100, 700), random.randint(100, 500)
            distractors.append({'x': x, 'y': y, 'radius': 20, 'color': 'green'})

        # Combine all the objects
        objects_list = [start_button, target] + distractors

        # Draw each object
        for obj in objects_list:
            self.canvas.create_oval(obj['x'] - obj['radius'], obj['y'] - obj['radius'],
                                    obj['x'] + obj['radius'], obj['y'] + obj['radius'],
                                    fill=obj['color'], tags=f"object_{objects_list.index(obj)}")
        return objects_list  # Return list of objects created

    def highlight_object(self, object_index):
        obj = self.objects[object_index]      # Get the object based on its index
        # Change selected object's color to yellow
        self.canvas.itemconfig(f"object_{object_index}", fill='yellow')