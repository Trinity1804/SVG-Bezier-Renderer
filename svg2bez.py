from svgpathtools import svg2paths

def svg_to_desmos(svg_file):
    paths, _ = svg2paths(svg_file)
    desmos_equations = []
    for path in paths:
        for segment in path:
            if type(segment).__name__ == 'CubicBezier':
                bpoints = segment.bpoints()
                equation_x = "{}*(1-t)^3 + 3*{}*(1-t)^2*t + 3*{}*(1-t)*t^2 + {}*t^3".format(*[p.real for p in bpoints])
                equation_y = "{}*(1-t)^3 + 3*{}*(1-t)^2*t + 3*{}*(1-t)*t^2 + {}*t^3".format(*[p.imag for p in bpoints])
                desmos_equations.append((equation_x, equation_y))
        
    return desmos_equations

filename = input('enter file path: ')
equations = svg_to_desmos(filename)

f = open("output.txt", "x")

with open("output.txt", "w") as f:
    for i, (x, y) in enumerate(equations):
        flipped_y = "-(" + y + ")"
        f.write(f'({x}, {flipped_y})\n')
