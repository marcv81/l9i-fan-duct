import svgwrite

def centered_square(center, r, fill=None):
    return svgwrite.shapes.Rect(insert=(center[0]-r, center[1]-r), size=(2*r, 2*r), fill=fill)

def generate(filename, width=92, extra_width=0, hole_spacing=82.5, hole_diameter=3):

    drawing = svgwrite.Drawing(filename, size=('210mm', '297mm'), viewBox=('0 0 210 297'))

    # Square outline
    drawing.add(centered_square((0, 0), (width+extra_width)/2, fill='red'))
    drawing.add(centered_square((0, 0), (hole_spacing)/2, fill='green'))

    # Mounting holes
    for center in (
        (-hole_spacing/2, -hole_spacing/2),
        (-hole_spacing/2,  hole_spacing/2),
        ( hole_spacing/2, -hole_spacing/2),
        ( hole_spacing/2,  hole_spacing/2)
    ):
        drawing.add(svgwrite.shapes.Circle(center=center, r=(width-hole_spacing)/2, fill='yellow'))
        drawing.add(svgwrite.shapes.Circle(center=center, r=hole_diameter/2, fill='blue'))

    # Outer rounding
    rounded_radius = width/2 - hole_spacing/2
    rounded_center = (width+extra_width)/2 - rounded_radius
    if extra_width > 0:
        for center in (
                (-rounded_center, -rounded_center),
                (-rounded_center,  rounded_center),
                ( rounded_center, -rounded_center),
                ( rounded_center,  rounded_center)):
            drawing.add(svgwrite.shapes.Circle(center=center, r=rounded_radius, fill='yellow'))
    for position in (
            (-rounded_center-rounded_radius, -rounded_center-rounded_radius),
            (-rounded_center-rounded_radius,  rounded_center),
            ( rounded_center,                -rounded_center-rounded_radius),
            ( rounded_center,                 rounded_center)):
        drawing.add(svgwrite.shapes.Rect(insert=position, size=(rounded_radius, rounded_radius), fill='green'))

    drawing.save()

generate('bottom.svg')
generate('top.svg', extra_width=40)
