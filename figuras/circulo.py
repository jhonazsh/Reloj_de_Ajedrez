import OpenGL 
from OpenGL.GL import *
from OpenGL.GLUT import *
from math import sin,cos,sqrt,pi

class circulo:
	def draw(self):
		PI=3.1415926535898
		circle_points = 100
		glBegin(GL_LINE_LOOP)

		for i in range(circle_points): 
			glColor3f(1.0, 1.0, 1.0)
			angle = 2*PI*i/circle_points
			glVertex2f(cos(angle), sin(angle))
		glEnd()
