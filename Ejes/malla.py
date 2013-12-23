import OpenGL 
from OpenGL.GL import *
from OpenGL.GLUT import *

class malla:
	def draw(self):
		dis=0
		while dis <= 140:
			glColor3ub(0,255,0)
			glBegin(GL_LINES)
			glVertex3f(-140,0,dis)
			glVertex3f(140,0,dis) 

			glVertex3f(-140,0,-dis)
			glVertex3f(140,0,-dis)
			glEnd()
			dis=dis+5

		dis=0

		while dis <= 140:
			glBegin(GL_LINES)
			glVertex3f(dis,0,-140)
			glVertex3f(dis,0,140) 

			glVertex3f(-dis,0,-140)
			glVertex3f(-dis,0,140)
			glEnd()
			dis=dis+5
