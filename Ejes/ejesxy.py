import OpenGL 
from OpenGL.GL import *
from OpenGL.GLUT import *

class Ejes():
  #ATRIBUTOS o caracteristicas de los Ejes
  (xmin, xmax) = (-100,100)
  (ymin, ymax) = (-100,100)
  (zmin, zmax) = (-100,100)
  #colores de los ejes
  xColor = [255,0,0]# Rojo
  yColor = [0,255,0]# Verde
  zColor = [0,0,255]# Azul  
  
  #Metodo o Comportamiento, que define la graficacion de los Ejes
  #El parametro self es obligatorio, hace referencia al objeto actual
  def draw(self):
    #necesitamos la variable self, para acceder a los atributos 
    glBegin(GL_LINES)
    #Eje X de rojo
    glColor3ubv(self.xColor)
    glVertex3f(self.xmin,   0.0,   0.0)
    glVertex3f(self.xmax,   0.0,   0.0)
    #Eje Y de Verde
    glColor3ubv(self.yColor)
    glVertex3f(  0.0, self.ymin,   0.0)
    glVertex3f(  0.0, self.ymax,   0.0)
    #Eje Z de Azul
    glColor3ubv(self.zColor)
    glVertex3f(  0.0,   0.0, self.zmin)
    glVertex3f(  0.0,   0.0, self.zmax)
    glEnd()     
    pass # esta funcion no hace nada