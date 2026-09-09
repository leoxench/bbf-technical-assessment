def print_circle(width=48, height=40, radius=0.78, thickness=0.08):
    """
    Print a circular outline using dots on a '#' background.

    The coordinates are normalized so the circle keeps its shape even when
    width and height are different.
    """
    for row in range(height):
        line = []

        for col in range(width):
            # Normalize the current character position around the center.
            x = (col - (width - 1) / 2) / (width / 2)
            y = (row - (height - 1) / 2) / (height / 2)

            distance = (x * x + y * y) ** 0.5

            if abs(distance - radius) <= thickness:
                line.append(".")
            else:
                line.append("#")

        print("".join(line))


if __name__ == "__main__":
    print_circle()
