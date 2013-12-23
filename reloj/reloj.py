import OpenGL 
from OpenGL.GL import *
from OpenGL.GLUT import *

from figuras import cuadrado, circulo, equis, ve, aguja
from Ejes import ejesxy



#Objeto de la clase cuadrado, con su respectivo valos inicializado para forma I en romanos
cuadrado_uno = cuadrado.cuadradito()
cuadrado_uno.inicializar(1,8)


#Objeto de la clase circulo
circulito = circulo.circulo()

#Objeto de la clase equis, con su respectivo valor inicializado formando una X en romanos
equis_romano = equis.equis()
equis_romano.inicializar(15,8)

#Objeto de la clase ve, con su respectivo valor inicializado formando una V en romanos
vesita = ve.ve()
vesita.inicializar(17,5)

#Objeto de la clase aguja, con su respectivo valor inicializado para el horario
horario = aguja.aguja()
horario.inicializar(100,10)

#Objeto de la clase aguja, con su respectivo valor inicializado para el minutero
minutero = aguja.aguja()
minutero.inicializar(60,10)

#Objeto de la clase aguja, con su respectivo valor inicializado para el segundero
segundero = aguja.aguja()
segundero.inicializar(100,2)


class reloj:


	def draw(self, angle, valor):

		self.angle =angle
		self.valor = valor


		glColor3ub(49,49,49)
		glPushMatrix()
		glRotatef(-self.valor, 0.0, 0.0, 1.0)
		glRotatef(-0.0005*self.angle, 0.0, 0.0, 1.0)
		horario.draw()
		glPopMatrix()


		glColor3ub(84,84,84)
		glPushMatrix()
		glRotatef(-self.valor, 0.0, 0.0, 1.0)
		glRotatef(-0.01*self.angle, 0.0, 0.0, 1.0)
		minutero.draw()
		glPopMatrix()

		glColor3ub(0,0,0)
		glPushMatrix()
		glRotatef(-self.valor, 0.0, 0.0, 1.0)
		glRotatef(-self.angle, 0.0, 0.0, 1.0)
		segundero.draw()
		glPopMatrix()

		glColor3ub(0,0,0)
		glPushMatrix()
		glTranslatef(3,89.5,0)
		cuadrado_uno.draw()
		glPopMatrix()



		glPushMatrix()
		glTranslatef(6.5,89.5,0)
		cuadrado_uno.draw()
		glPopMatrix()

		glPushMatrix()
		glTranslatef(3,-90,0)
		cuadrado_uno.draw()
		glPopMatrix()

		glPushMatrix()
		glTranslatef(-95,0,0)
		cuadrado_uno.draw()
		glPopMatrix()

	    #******** Tres en romanos ********
		glPushMatrix()  
		glTranslatef(95,0,0)
		cuadrado_uno.draw()
		glPopMatrix()

		glPushMatrix()  
		glTranslatef(91,0,0)
		cuadrado_uno.draw()
		glPopMatrix()

		glPushMatrix() 
		glTranslatef(87,0,0)
		cuadrado_uno.draw()    
		glPopMatrix()
	    #*********************************
	    
		glPushMatrix()
		glTranslatef(-88.5,0,0)
		equis_romano.draw()
		glPopMatrix()
	  
		glPushMatrix()
		glTranslatef(-3,90,0)
		equis_romano.draw()
		glPopMatrix()
	  
		glPushMatrix()
		glTranslatef(-2,-90,0)
		vesita.draw()
		glPopMatrix()

		glColor3ub(0,0,0)
		glPushMatrix()
		glScalef(100,100,100)
		circulito.draw()
		glPopMatrix()

		"""
		for i in range(100):
			glColor3ub(255,0,0)
			glPushMatrix()

			glScalef(i,i,i)
			circulito.draw()
			glPopMatrix()

		for i in range(100):
			glColor3ub(255,0,0)
			glPushMatrix()

			glScalef(i+0.5,i+0.5,i+0.5)
			circulito.draw()
			glPopMatrix()
		"""

		