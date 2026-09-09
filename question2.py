class CircleRenderer:
    def __init__(self, width=48, height=40, radius=0.78, thickness=0.08):
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be greater than zero")

        if not 0 < radius < 1:
            raise ValueError("radius must be between 0 and 1")

        if thickness <= 0:
            raise ValueError("thickness must be greater than zero")

        self.width = width
        self.height = height
        self.radius = radius
        self.thickness = thickness

    def _distance_from_center(self, row, col):
        x = (col - (self.width - 1) / 2) / (self.width / 2)
        y = (row - (self.height - 1) / 2) / (self.height / 2)
        return (x * x + y * y) ** 0.5

    def render(self):
        rows = []

        for row in range(self.height):
            line = []

            for col in range(self.width):
                distance = self._distance_from_center(row, col)

                if abs(distance - self.radius) <= self.thickness:
                    line.append(".")
                else:
                    line.append("#")

            rows.append("".join(line))

        return "\n".join(rows)

    def print(self):
        print(self.render())


if __name__ == "__main__":
    circle = CircleRenderer()
    circle.print()
