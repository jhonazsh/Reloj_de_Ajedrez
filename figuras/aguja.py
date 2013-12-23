import OpenGL 
from OpenGL.GL import *
from OpenGL.GLUT import *

class aguja:
    def inicializar(self,l,a):
        self.largo=l
        self.ancho=a

    def draw(self):
        glBegin(GL_QUADS)
        glVertex3f(0,0,0)
        glVertex3f(self.largo/2,-self.ancho/2,0)
        glVertex3f(self.largo,0,0)
        glVertex3f(self.largo/2,self.ancho/2,0)
        glEnd()