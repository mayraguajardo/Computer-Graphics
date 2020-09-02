from diamond import Diamond
from teseract import Tesseract
diamonds = [Diamond(100,100), Diamond(100,100,-1)]
my_shader = None
tesseract = Tesseract(200)
tesseractMini = Tesseract(100)

def setup():
    global my_shader
    fullScreen(P3D, 3)
    smooth(8)
    my_shader = loadShader('frag.glsl','vert.glsl')
    
def draw():
    background("#FFFFFF")
    shader(my_shader, TRIANGLES)
    pointLight(255, 255, 255, width/2, height, 200);
    tesseractMini.setTexture(loadImage("texture1.jpg"));
    tesseractMini.display(600,290)
    tesseract.display(570,240)
    
    
    
    translate(width/2, height/2)
    
    
    fill(52, 192, 235, 80)
    stroke(255)
 
    
    if mousePressed and mouseX < width/2: fill(255,255,255)
    diamonds[0].display(200,200)
    diamonds[0].display(200,height-200)
    fill(52, 192, 235, 80)
    if mousePressed and mouseX > width/2: fill(255,255,255)
    diamonds[1].display(width-200,200)
    diamonds[1].display(width-200,height-200)
    
    try:
        if keyPressed and key in 'wW':
            diamonds[0].incrementXAngle()
            tesseract.incrementXAngle()
        elif keyPressed and key in 'sS':
            diamonds[0].decrementXAngle()
            tesseract.decrementXAngle()
        elif keyPressed and key in 'aA':
            diamonds[0].incrementYSpeed()
            tesseract.incrementYSpeed()
        elif keyPressed and key in 'dD':
            diamonds[0].decrementYSpeed()
            tesseract.decrementYSpeed()
    except:
        print('Key not found')
    
