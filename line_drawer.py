from scene import *

class MyScene (Scene):
	def setup(self):
		self.lines = []
		
	def touch_began(self, touch):
		x = touch.location.x
		y = touch.location.y
		self.xybegin = Point(x,y)
		print "Touch began at (%s, %s)" % (x, y)

	def touch_ended(self, touch):
		x = touch.location.x
		y = touch.location.y
		self.lines.append((self.xybegin.x, self.xybegin.y, x, y))
		print "Touch ended at (%s, %s)" % (x, y)
	
	def draw(self):
		background(0, 0, 0)
		fill(1, 0, 0)
		stroke(1, 0, 0)
		stroke_weight(3)
		
		for touch in self.touches.values():
			x = touch.location.x
			y = touch.location.y
			line(self.xybegin.x, self.xybegin.y, x, y)
			
		for l in self.lines:
			line(*l)

run(MyScene())