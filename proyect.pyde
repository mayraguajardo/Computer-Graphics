from diamond import Diamond

diamonds = [Diamond(100,100), Diamond(100,100,-1)]
my_shader = None

def setup():
    global my_shader
    fullScreen(P3D, 3)
    smooth(8)
    my_shader = loadShader('frag.glsl','vert.glsl')
    
def draw():
    background(0)
    shader(my_shader, TRIANGLES)
    pointLight(255, 255, 255, width/2, height, 200);
    
    translate(width/2, height/2)
    
    
    fill(0,255,0, 80)
    stroke(255)
    if mousePressed and mouseX < width/2: fill(255,255,255)
    diamonds[0].display(200,200)
    diamonds[0].display(200,height-200)
    fill(0,255,0, 80)
    if mousePressed and mouseX > width/2: fill(255,255,255)
    diamonds[1].display(width-200,200)
    diamonds[1].display(width-200,height-200)
    
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
    
