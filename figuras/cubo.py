import OpenGL 
from OpenGL.GL import *
from OpenGL.GLUT import *

class cubo:

	def draw(self):
		glBegin(GL_QUADS)
		glVertex3f(-2, 2,1)
		glVertex3f(2, 2,1)
		glVertex3f(2, -2,1)
		glVertex3f(-2, -2,1)

		glVertex3f(2, 2,-1)
		glVertex3f(2, -2,-1)
		glVertex3f(-2, -2,-1)
		glVertex3f(-2, 2,-1)

		glVertex3f(-2, 2,1)
		glVertex3f(-2, 2,-1)
		glVertex3f(-2, -2,-1)
		glVertex3f(-2, -2,1)

		glVertex3f(2, 2,1)
		glVertex3f(2, 2,-1)
		glVertex3f(2, -2,-1)
		glVertex3f(2, -2,1)

		glVertex3f(-2, 2,1)
		glVertex3f(-2, 2,-1)
		glVertex3f(2, 2,-1)
		glVertex3f(2, 2,1)

		glVertex3f(-2, -2,1)
		glVertex3f(-2, -2,-1)
		glVertex3f(2, -2,-1)
		glVertex3f(2, -2,1)
		glEnd()