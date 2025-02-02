# SVG Bezier Renderer

A simple Python program to render .svg files as bezier curve equations, to render in a graphing calculator.

## Usage

Install required library:

```bash
pip install svgpathtools
```

Run `svg2bez.py`:

```bash
python3 svg2bez.py
```

Input the SVG file's path when prompted to do so.

The equations will be written to an output file (`output.txt`) in your current working directory.

Paste these equations into a graphing calculator like [Desmos](https://www.desmos.com/calculator), to render the image.

## Explanation

SVG (Scalable Vector Graphic) files are comprised of equations, called `Bezier Curves`. Bezier curves have multiple forms, such as cubic, quadratic, etc. Cubic bezier curves take an input of 4 points on a plane, and output a curve that does not necessarily pass through these points, but is defined by these points. By combining multiple bezier curves, we can create images. This is what happens in an SVG file. My program extracts these equations and outputs them in a text file. These equations can be pasted into a graphing calculator like Desmos, to render the image.
