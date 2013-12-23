import OpenGL 
from OpenGL.GL import *
from OpenGL.GLUT import *

class ve:
	def inicializar(self,l,a):
		self.largo=l
		self.ancho=a

	def draw(self):
		glBegin(GL_QUADS)
		glVertex3f(-(self.ancho/2)-2.5, self.largo/2,0)
		glVertex3f(-self.ancho/4, self.largo/2,0)
		glVertex3f(self.ancho/4, -self.largo/2,0)
		glVertex3f(-self.ancho/4, -self.largo/2,0)
		glEnd()

		glBegin(GL_QUADS)
		glVertex3f(self.ancho/4, self.largo/2,0)
		glVertex3f((self.ancho/2)+1.5, self.largo/2,0)
		glVertex3f(self.ancho/4, -self.largo/2,0)
		glVertex3f(-self.ancho/4, -self.largo/2,0)
		glEnd()