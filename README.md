# SVGTutle

This is a rudimentary turtle geometry module that is working reasonably well in Jupyter and Collabratory.
```python
t = Turtle(200, 200)

def arc(s):
  for i in range(10):
    t.forward(s)
    t.right(9)

def leaf(s):
  t.push()
  arc(s)
  t.right(90)
  arc(s)
  t.pop()

t.set_color("green")
t.forward(25)
t.left(90)
t.forward(25)
t.push()
t.set_color("lightgreen")
leaf(5)
t.pop()
t.forward(10)

t.d.saveSvg("output.svg")
t.d  # Display as SVG
```
