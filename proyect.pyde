from diamond import Diamond

speed = 0.05
diamond = Diamond(100,100, -1)
my_shader = None

def setup():
    global my_shader
    fullScreen(P3D, 3)
    smooth(8)
    my_shader = loadShader('frag.glsl','vert.glsl')
    
def draw():
    global diamonds_angle, speed, my_shader
    background(0)
    
    translate(width/2, height/2, -50)
    pointLight(255,255,255 ,200, 200, 0)
    
    fill(0,255,0,80)
    diamond.display(200,200)
    
    
    
    if keyPressed and key in 'wW':
        diamond.incrementXAngle()
    elif keyPressed and key in 'sS':
        diamond.decrementXAngle()
    elif keyPressed and key in 'aA':
        diamond.incrementYSpeed()
    elif keyPressed and key in 'dD':
        diamond.decrementYSpeed()
        
    # if mouseX < 300 and mouseX > 140 and mouseY < 300 and mouseY > 115:
    #     fill(10,255,10)
    # else:
    #     fill(0,255,0)
        
    # pushMatrix()
    # translate(-width/2+200,-height/2+200, 0)
    # rotateX(diamonds_angle['1.2'])
    # pushMatrix()
    # rotateY(diamonds_angle['1'])
    # diamonds_angle['1'] += speed
    # diamond(100,100)
    # popMatrix()
    # popMatrix()
    
    # if mouseX < 300 and mouseX > 140 and mouseY < 300 and mouseY > 115:
    #     fill(10,255,10)
    # else:
    #     fill(0,255,0)
    
    # pushMatrix()
    # translate(width/2-200,-height/2+200, 0)
    # rotateX(diamonds_angle['2.2'])
    # pushMatrix()
    # rotateY(diamonds_angle['2'])
    # diamonds_angle['2'] += speed
    # diamond(100,100)
    # popMatrix()
    # popMatrix()
    
    
    
    
    
def mousePressed():
    print(mouseX, mouseY)
