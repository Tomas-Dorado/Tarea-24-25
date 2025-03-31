class Entity:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self):
        # Placeholder for drawing logic
        print(f"Drawing entity at ({self.x}, {self.y}) with image {self.image}")