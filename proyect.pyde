from diamond import Diamond

speed = 0.05
diamonds = [Diamond(100,100), Diamond(100,100,-1)]
my_shader = None

def setup():
    global my_shader
    fullScreen(P3D, 3)
    smooth(8)
    my_shader = loadShader('frag.glsl','vert.glsl')
    
def draw():
    global diamonds_angle, speed, my_shader
    background(0)
    shader(my_shader)
    pointLight(255, 255, 255, width/2, height, 500);
    
    translate(width/2, height/2)
    noStroke()
    pushMatrix()
    translate(mouseX-width/2, mouseY-height/2)
    if mousePressed:
        fill(255,0,0)
    else:
        fill(0,0,0,0)
    sphere(50)
    popMatrix()
    
    fill(0,255,0)
    diamonds[0].display(200,200)
    diamonds[1].display(width-200,200)
    
    try:
        if keyPressed and key in 'wW':
            diamonds[0].incrementXAngle()
        elif keyPressed and key in 'sS':
            diamonds[0].decrementXAngle()
        elif keyPressed and key in 'aA':
            diamonds[0].incrementYSpeed()
        elif keyPressed and key in 'dD':
            diamonds[0].decrementYSpeed()
    except:
        print('Key not found')
        
    # if mouseX < 300 and mouseX > 140 and mouseY < 300 and mouseY > 115:
    #     fill(10,255,10)
    # else:
    #     fill(0,255,0)
    
    # if mouseX < 300 and mouseX > 140 and mouseY < 300 and mouseY > 115:
    #     fill(10,255,10)
    # else:
    #     fill(0,255,0)

    
    
    
    
def mousePressed():
    print(mouseX, mouseY)
