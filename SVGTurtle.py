import drawSvg as draw
import math
DEG2RAD = math.pi/180

class state:
  def __init__(self, x, y, heading, pendown, color):
    self.x = x
    self.y = y
    self.heading = heading
    self.pendown = pendown
    self.color = color

class Turtle:
  def __init__(self, w=400, h=400):
    self.stack = []
    self.d = draw.Drawing(w, h, origin='center')
    self.d.setPixelScale(2)
    self.x = 0
    self.y = 0
    self.heading = 0
    self.pendown = True
    self.color = "#00eeee"

  def push(self):
    s = state(self.x, self.y, self.heading, self.pendown, self.color)
    self.stack.append( s )
  
  def pop(self):
    s = self.stack.pop()
    self.x = s.x
    self.y = s.y
    self.heading = s.heading
    self.pendown = s.pendown
    self.color = s.color

  def _line(self, x1, y1, x2, y2):
    self.d.append(draw.Lines(x1, y1, x2, y2,
                          close=False,
                          fill=None,
                          stroke=self.color))
  
  def forward(self, d):
    nx = self.x + math.cos(self.heading * DEG2RAD) * d
    ny = self.y + math.sin(self.heading * DEG2RAD) * d
    if self.pendown:
      self._line(self.x, self.y, nx, ny)
    self.x = nx
    self.y = ny
  
  def rectangle(self, w, h):
    # does not move the turtle
    self.d.append(draw.Rectangle(x=self.x, y=self.y, width=w, height=h, stroke=self.color, fill="rgba(0,0,0,0)"))

  def pen_down(self):
    self.pendown = True
  
  def pen_up(self):
    self.pendown = False

  def right(self, delta):
    self.heading -= delta
  
  def left(self, delta):
    self.heading += delta

  def set_color(self, c):
    self.color = c
  
  def jump_to(self, x, y):
    self.x = x
    self.y = y
