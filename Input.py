from OpenGL.GL import *
from glew_wish import *
import glfw

pos_x_triangulo = 0
pos_y_triangulo = 0

tiempo = 0.0
tiempoAnterior = 0.0

velocidad = 0.8

def actualizar (window):
    global velocidad
    global tiempo
    global tiempoAnterior
    global pos_x_triangulo
    global pos_y_triangulo

    tiempo = glfw.get_time()

    tiempoDiferencial = tiempo - tiempoAnterior

    estado_tecla_izquierda = glfw.get_key(window, glfw.KEY_LEFT)
    estado_tecla_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estado_tecla_abajo = glfw.get_key(window, glfw.KEY_DOWN)
    estado_tecla_arriba = glfw.get_key(window, glfw.KEY_UP)

    cantidadMovimiento = velocidad * tiempoDiferencial

    if estado_tecla_izquierda == glfw.PRESS:
        pos_x_triangulo = pos_x_triangulo - cantidadMovimiento
    if estado_tecla_derecha == glfw.PRESS:
        pos_x_triangulo = pos_x_triangulo + cantidadMovimiento
    if estado_tecla_abajo == glfw.PRESS:
        pos_y_triangulo = pos_y_triangulo - cantidadMovimiento
    if estado_tecla_arriba == glfw.PRESS:
        pos_y_triangulo = pos_y_triangulo + cantidadMovimiento

    tiempoAnterior = tiempo

def dibujar():
    global pos_x_triangulo
    global pos_y_triangulo
    #rutinas de dibujo
    glPushMatrix()
    glTranslate(pos_x_triangulo, pos_y_triangulo, 0)
    glColor3f(0.1,0.4,0.6)
    glBegin(GL_TRIANGLES)
    glVertex3f(0,0.1,0)
    glVertex3f(-0.1,-0.1,0)
    glVertex3f(0.1,-0.1,0)
    glEnd()
    glPopMatrix()

def key_callback(window, key, scancode, action, mods):

    global pos_x_triangulo
    global pos_y_triangulo
    #if key == glfw.KEY_ESCAPE:
        #if action == glfw.PRESS:
            #print("Se detectó un press")
        #if action == glfw.RELEASE:
            #print("Se detectó un release")
        #if action == glfw.REPEAT:
            #print("Se detectó un repeawt")

    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, 1)

    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_LEFT:
            pos_x_triangulo = pos_x_triangulo -0.05

        if key == glfw.KEY_RIGHT:
            pos_x_triangulo = pos_x_triangulo +0.05

        if key == glfw.KEY_DOWN:
            pos_y_triangulo = pos_y_triangulo -0.05

        if key == glfw.KEY_UP:
            pos_y_triangulo = pos_y_triangulo +0.05


def main():
    global tiempo
    global tiempoAnterior
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(800,600,"Mi ventana", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    #glfw.set_key_callback(window, key_callback)
    tiempo = glfw.get_time()
    tiempoAnterior = glfw.get_time()
    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,800,600)
        #Establece color de borrado
        glClearColor(0.4,0.6,0.6,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Actualizar valores de la app
        actualizar(window)
        #Dibujar
        dibujar()
        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()