import OpenGL 
from OpenGL.GL import *
from OpenGL.GLUT import *
from figuras import cubo

#Definimos un objeto de la clase cubo
cubito = cubo.cubo()

class cuerpoReloj:
	def draw(self):
		#Union entre los dos relojes
		glColor3ub(255,218,185)
		glPushMatrix()
		glScalef(5,10,5)
		cubito.draw()
		glPopMatrix()

		#Cobertor del reloj derecho
		glColor3ub(0,255,0)
		glPushMatrix()
		glTranslatef(-50,0,0)
		glScalef(20,20,10)
		cubito.draw()
		glPopMatrix()
		
		#Cobertor del reloj izquierdo
		glColor3ub(0,255,0)
		glPushMatrix()
		glTranslatef(50,0,0)
		glScalef(20,20,10)
		cubito.draw()
		glPopMatrix()

		#boton
		glColor3ub(255,218,185)
		glPushMatrix()
		glTranslatef(-50,-41,0)
		glScalef(2,3,2)
		cubito.draw()
		glPopMatrix()

		glColor3ub(255,218,185)
		glPushMatrix()
		glTranslatef(50,-41,0)
		glScalef(2,3,2)
		cubito.draw()
		glPopMatrix()

		#
		glColor3ub(0,100,0)
		glPushMatrix()
		glTranslatef(-50,-48,0)
		glScalef(5,0.5,7)
		cubito.draw()
		glPopMatrix()

		glColor3ub(0,100,0)
		glPushMatrix()
		glTranslatef(50,-48,0)
		glScalef(5,0.5,7)
		cubito.draw()
		glPopMatrix()


		#Superficie menor del reloj
		glColor3ub(84,84,84)
		glPushMatrix()
		glTranslatef(0,44,0)
		glScalef(60,2,30)
		cubito.draw()
		glPopMatrix()

		#Superficie base del reloj
		glColor3ub(49,49,49)
		glPushMatrix()
		glTranslatef(0,52,0)
		glScalef(65,2,35)
		cubito.draw()
		glPopMatrix()