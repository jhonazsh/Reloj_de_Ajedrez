import OpenGL 
from OpenGL.GL import *
from OpenGL.GLUT import *

class cuadradito:
	def inicializar(self,l,a):
		self.largo=l
		self.ancho=a

	def draw(self):
		glBegin(GL_QUADS)
		glVertex3f(-self.largo, -self.ancho,0)
		glVertex3f(-self.largo, self.ancho,0)
		glVertex3f( self.largo, self.ancho,0)
		glVertex3f( self.largo, -self.ancho,0)
		glEnd()