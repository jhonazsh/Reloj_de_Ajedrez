# -*- coding: utf-8 -*- 
#________________ IMPORTANDO MODULOS Y PAQUETES NECESARIOS ________________
import OpenGL 

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys, time 
from math import sin,cos,sqrt,pi
from OpenGL.constants import GLfloat
vec4 = GLfloat_4
from numpy import *

from figuras import cuadrado, cubo
from Ejes import ejesxy, malla
from reloj import reloj, cuerpoReloj
#__________________________________________________________________________

#Definiendo variables paa el uso del teclado
des=0; des1=0; des2=0; des3=0; des4=0; des5=0; des6=0; des7=0

#Definimos un objeto global, para los ejes
ejesitos = ejesxy.Ejes()

#Definimos el objeto global, para la clase reloj
relojito = reloj.reloj()

#Definimos un objeto de la clase cuadrado
cuadrado_grande = cuadrado.cuadradito()
cuadrado_grande.inicializar(10,20)

#Definimos un objeto de la clase cubo
cubito = cubo.cubo()

#Definimos un objeto de la clase malla
mallita = malla.malla()

#Definimos un objeto de la clase cuerpoReloj
cuerpitoReloj = cuerpoReloj.cuerpoReloj()

#-------------------- porcion aun desconocida -------------------
(view_rotx,view_roty,view_rotz)=(0.0, 0.0, 0.0)
angle = 0.0

tStart = time.time()
tAnt = tStart
#----------------------------------------------------------------

valor_izquierda = 270
valor_derecha = 90

#Función que dibuja a todas las figuras dentro del frame o ventana
def draw():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(10,5,10,0,0,0,0,1,0);
    glRotatef(view_rotx, 1.0, 0.0, 0.0)
    glRotatef(view_roty, 0.0, 1.0, 0.0)
    glRotatef(view_rotz, 0.0, 0.0, 1.0)

    glRotatef(180+des,1,0,0)
    glRotatef(180+des1,0,1,0)
    glRotatef(-360+des2,0,0,1)

    #Descomentar la siguiente linea, si queremos ver los ejes x, y, z
    #ejesitos.draw()

    #El Objeto mallita se dibuja
    mallita.draw()

    glTranslatef(0,-60,0)

    #Reloj Izquierdo
    glPushMatrix()
    glScalef(-0.35,-0.35,1)
    glTranslatef(-140,0,12)
    relojito.draw(angle, valor_izquierda)
    glPopMatrix()

    #Reloj Derecho
    glPushMatrix()
    glScalef(-0.35,-0.35,1)
    glTranslatef(140,0,12)
    relojito.draw(angle, valor_derecha)
    glPopMatrix()

    #Dibujando el cuerpo del reloj
    cuerpitoReloj.draw()

    glutSwapBuffers()



def idle():
    global tStart, tAnt, angle
    t = time.time()
    
    if t - tAnt >= 1:
        tAnt = t
        angle = angle + 5
        
        glutPostRedisplay()

def reshape(width, height):
    h = float(height) / float(width);
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #gluPerspective(90.0,width/height,1,100);
    #glFrustum(-20.0, 50.0, -h, h, 5.0, 60.0)
    glOrtho(-160,160,-160,160,-160,160)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -40.0)

def init():
    #glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_NORMALIZE)

def visible(vis):
    if vis == GLUT_VISIBLE:
        glutIdleFunc(idle)
    else:
        glutIdleFunc(None)

def keyboard(key, x, y):
    global des, des1, des2, des3, des4, des5, des6, des7    
    
    if key == "q":
        print "muevete"
        des3 = des3 + 1
    if key == "a":
        des5 = des5 + 1
    if key == "z":
        des6 = des6 + 1
    if key == "x":
        des7 = des7 + 1
    if key == "t":
        des4 = des4 + 1
    if key == "w":
        des = des + 1
    if key == "e":
        des2 = des2 + 1
    if key == "r":
        des1 = des1 + 1
    if key == "s":
        des = des - 1     
    if key == "d":
        des1 = des1 - 1
    if key == "f":
        des2 = des2 - 1
    glutPostRedisplay()


if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)

    glutInitWindowPosition(0, 0)
    glutInitWindowSize(700, 700)
    glutCreateWindow("Reloj de Ajedrez")
    init()
    
    glutDisplayFunc(draw)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    #glutSpecialFunc(special)
    glutVisibilityFunc(visible)

    glutMainLoop()
