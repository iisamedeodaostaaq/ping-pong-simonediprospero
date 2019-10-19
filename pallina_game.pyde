xpos = 60 
ypos = 60
b_height = 400;
b_width= 500;
x_dir = 1
y_dir = 1
x_racchetta= 200
x_racchetta1= 200
punt=0;
punt1=0;

def setup():
    global xpos,ypos,b_width,b_height
    background(18,3,255)
    size (b_width, b_height)
    

def draw():
    global xpos,ypos,b_width,b_height,x_dir,y_dir, x_racchetta, x_racchetta1,punt,punt1
    background(18,3,255)
    ellipse(xpos,ypos,50,50)
    
    
    
    rect(x_racchetta,375,100,25)
    rect(x_racchetta1,0,100,25)

    
    if (ypos+25>height-25) and (xpos+25)>x_racchetta and (xpos-25)<(x_racchetta+100) :
        y_dir = -1
        punt+=1
        
    
    if (ypos-25<25) and (xpos+25)>x_racchetta1 and (xpos-25)<(x_racchetta1+100) :
        y_dir = +1
        punt1+=1
        
    if (xpos+25 > width or xpos-25 < 0):
        x_dir = x_dir * (-1)
        fill(random (0, 255),random (0, 255),random (0, 255))
        
    
        
    if (ypos+25 > height or ypos-25 < 0):
        y_dir = y_dir * (-1)
        fill(random (0, 255),random (0, 255),random (0, 255))

    xpos = xpos+5*x_dir
    ypos = ypos+5*y_dir
    
        

    textSize(20)
    text(punt,0,400)
    
    textSize(20)
    text(punt1, 0,20)
    
    
def keyPressed():
    global x_racchetta,x_racchetta1
    if  keyCode == LEFT:
        x_racchetta -= 10
    if  keyCode == RIGHT:
        x_racchetta += 10
        
    if key== "z":
        x_racchetta1 -= 10
    if key== "x":
        x_racchetta1 += 10
