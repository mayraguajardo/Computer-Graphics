class Tesseract:
    
    def __init__(self, size, *multiplier):
        
        self.size = size
        self.y_angle = 0
        self.x_angle = 0
        self.y_speed = 1
        if len(multiplier) > 0:
            self.multiplier = multiplier[0]
        else:
            self.multiplier = 1
    
    def incrementYSpeed(self):
        self.y_speed += 0.1 * self.multiplier
        
    def decrementYSpeed(self):
        self.y_speed -= 0.1 * self.multiplier
        
    def incrementXAngle(self):
        self.x_angle += 0.1 * self.multiplier
    
    def decrementXAngle(self):
        self.x_angle -= 0.1 * self.multiplier
    
    def display(self, x, y):
        img = loadImage("texture3.jpg")
        pushMatrix()
        translate(x + (self.size / 2), y + (self.size / 2), self.size / 2)
        rotateY(self.y_angle)
        rotateX(self.x_angle)
        translate(-x - (self.size / 2), -y - (self.size / 2), - self.size / 2)
        self.y_angle += 0.05 * self.y_speed * self.multiplier
        
        
        
        #izquierdo
        beginShape()
        vertex(x,  y, 0)
        vertex(x + self.size, y, 0)
        vertex(x + self.size, y + self.size, 0)
        vertex(x, y + self.size, 0)
        endShape(CLOSE)
        
        #derecho
        beginShape()
        vertex(x + self.size, y, 0)
        vertex(x + self.size, y, self.size)
        vertex(x + self.size, y + self.size, self.size)
        vertex(x + self.size, y + self.size, 0)
        endShape(CLOSE)
        
        #atras
        beginShape()
        vertex(x, y, self.size)
        vertex(x + self.size, y, self.size)
        vertex(x + self.size, y + self.size, self.size)
        vertex(x, y + self.size, self.size)
        endShape(CLOSE)
        
        #frente
        beginShape()
        vertex(x, y, 0)
        vertex(x, y, self.size)
        vertex(x, y + self.size, self.size)
        vertex(x, y + self.size, 0)
        endShape(CLOSE)
        popMatrix()
        
        
