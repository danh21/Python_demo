# Draws a box of stars with the given width and height.
def box(width, height, outline = "*"):
    print (width * outline)
    for i in range(height - 2):
        print (outline + (width - 2)*" " + outline)
    print (width * outline)

# main
print (13 * "*")
print (7 * "*")
print (35 * "*")

box(10, 3)
box(5, 4)