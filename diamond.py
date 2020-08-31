class Diamond:
    def __init__(self, base_length, half_height):
        self.base_length = base_length
        self.half_height = half_height
        self.y_angle = 0
        self.x_angle = 0
    
    def incrementYRotation(self):
        self.y_angle += 0.01 
    
    def display(self, x, y):
        pushMatrix()
        translate(-width/2+x,-height/2+y, 0)
        rotateX(self.x_angle)
        pushMatrix()
        rotateY(self.y_angle)
        self.y_angle += 0.05
        
        
        translate(-self.base_length/2,0, -(sin(PI/3)*self.base_length)/3)
    
        beginShape(TRIANGLES)
        vertex(0,0,0)
        vertex(self.base_length/2,0, sin(PI/3)*self.base_length)
        vertex(self.base_length,0,0)
        endShape()
    
        beginShape(TRIANGLES)
        vertex(0,0,0)
        vertex(self.base_length/2,0, (sin(PI/3)*self.base_length))
        vertex(self.base_length/2,-self.half_height, (sin(PI/3)*self.base_length)/3)
        endShape()
    
        beginShape(TRIANGLES)
        vertex(0,0,0)
        vertex(self.base_length,0,0)
        vertex(self.base_length/2,-self.half_height, (sin(PI/3)*self.base_length)/3)
        endShape()
    
        beginShape(TRIANGLES)
        vertex(self.base_length/2,0, (sin(PI/3)*self.base_length))
        vertex(self.base_length,0,0)
        vertex(self.base_length/2,-self.half_height, (sin(PI/3)*self.base_length)/3)
        endShape()
        
        
    
    
        beginShape(TRIANGLES)
        vertex(0,0,0)
        vertex(self.base_length/2,0, (sin(PI/3)*self.base_length))
        vertex(self.base_length/2,self.half_height, (sin(PI/3)*self.base_length)/3)
        endShape()
    
        beginShape(TRIANGLES)
        vertex(0,0,0)
        vertex(self.base_length,0,0)
        vertex(self.base_length/2,self.half_height, (sin(PI/3)*self.base_length)/3)
        endShape()
    
        beginShape(TRIANGLES)
        vertex(self.base_length/2,0, (sin(PI/3)*self.base_length))
        vertex(self.base_length,0,0)
        vertex(self.base_length/2,self.half_height, (sin(PI/3)*self.base_length)/3)
        endShape()

        popMatrix()
        popMatrix()
    
