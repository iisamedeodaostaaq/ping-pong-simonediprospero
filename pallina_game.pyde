x_Circle=0 #variabile coordinata x della pallina
y_Circle=0 #variabile coordinata y della pallina
circleWidth=40 #variabile larghezza pallina
circleHeight=40 #variabile altezza pallina
totalWidth=700 #variabile larghezza totale del campo di gioco
totalHeigth=500 #variabile altezza totale del campo di gioco
x_circleSpeed=3 #variabile velocita pallina coordinata x
y_circleSpeed=3 #variabile velocita pallina coordinata y
x_paddleLeft=25 #variabile coordinata x racchetta sinistra, il meno 25 lo si mette per distaccare di 25 la racchetta dal campo di gioco
y_paddleLeft=totalHeigth/2 #variabile coordinata y racchetta sinistra, in questo caso basta fare il quoziente tra l'altezza totale del campo di gioco e 2, poichè la racchetta si muove sull'asse y
paddleWidth=25 #variabile larghezza delle due racchette, sia sinistra che destra
paddleHeigth=100 #variabile altezza delle due racchette, sia destra che destra
paddleSpace = 5 #variabile racchetta che quando tocca il bordo del campo di gioco torna indietro di 5
x_paddleRight=totalWidth-25 #variabile coordinata x racchetta destra, in questo caso si fa la differenza tra la larghezza totale del campo di gioco e 25 cosi da posizionarla a specchio rispetto alla racchetta sinistra
y_paddleRight=totalHeigth/2 #variabile coordinata y racchetta destra, in questo caso basta fare il quoziente tra l'altezza totale del campo di gioco e 2, poichè la racchetta si muove sull'asse y
scoreLeft=0 #variabile inizializzo il punteggio del giocatore sinistra a 0
scoreRight=0 #variabile inizializzo il punteggio del giocatore destro a 0
winScore=5 #variabile punteggio massimo, il primo giocatore che riesce ad arrivare a 5 ha vinto
x_paddleSpacepeed=8 #variabile velocita racchetta coordinata x
y_paddleSpacepeed=8 #variabile velocita racchetta coordinata y


def setup():
    global x_Circle,y_Circle #variabili globali
    size(700,500); #dimensioni campo di gioco
    x_Circle= totalWidth/2 #posizionare la pallina al centro nella coordinata x
    y_Circle= totalHeigth/2 #posizionare la pallina al centro nella coordinata y
    rectMode(CENTER) #metodo per mettere le due racchette al centro del campo di gioco 
    textSize(25)#grandezza testo

    
def draw():
    global x_Circle,y_Circle,circleWidth,circleHeight,totalWidth,totalHeigth,x_circleSpeed, y_circleSpeed,x_paddleLeft, y_paddleLeft, paddleWidth, paddleHeigth, y_paddleLeft, paddleWidth
    background(0,0,0); #sfondo campo gioco
    drawLinea() #prototipo funzione che crea la linea in mezzo
    drawCircle() #prototipo funzione che disegna la pallina
    drawPaddle() #prototipo funzione che disegna le due racchette
    moveCircle() #prototipo funzione che fa muovere la pallina
    bounceOff() #prototipo funzione  che fa rimbalzzare la pallina sui bordi del campo
    contactPaddle() #prototipo funzione che fa rimbalzare la pallina quando tocca la racchetta
    restrictPaddle() #prototipo funzione che risolve i problemi di contatto tra pallina e a racchetta
    scores() #prototipo funzione che conta i punti ai 2 giocatori
    gameOver() #prototipo funzione che fa fermare il gioco, quando uno dei due giocatori riesce a vincere
    
def drawLinea():
    fill(255) #colore bianco per la linea in mezzo 
    rect(width/2,height/2, 2, 700); #creazione linea in mezzo
    
def drawCircle():
    global x_Circle,y_Circle,circleWidth,circleHeight
    fill(random(0,255),random(0,255),random(0,255)); #colora la pallina in modo randomico
    ellipse(x_Circle, y_Circle, circleWidth, circleHeight); #creazione pallina
    
def drawPaddle():
    global x_paddleLeft, y_paddleLeft, paddleWidth, paddleHeigth,x_paddleRight, y_paddleRight
    fill(255,0,0); #colore rosso per la racchetta sinistra
    rect(x_paddleLeft, y_paddleLeft, paddleWidth, paddleHeigth); #creazione racchetta sinistra
    fill(0,0,255); #colore blu per la racchetta destra
    rect(x_paddleRight, y_paddleRight, paddleWidth, paddleHeigth); #creazione racchetta destra
    
def moveCircle():
    global x_Circle,y_Circle,x_circleSpeed, y_circleSpeed
    x_Circle=x_Circle+x_circleSpeed; #far muovere la pallina attraverso la sua coordinata x
    y_Circle=y_Circle+y_circleSpeed; #far muovere la pallina attraverso la sua coordinata y

def bounceOff():
    global x_Circle,y_Circle,circleWidth, circleHeight,x_circleSpeed, y_circleSpeed, scoreLeft, scoreRight, totalHeigth, totalWidth
    if ( x_Circle > totalWidth - circleWidth/2 ):#se la x della pallina supera la larghezza totale
        setup()#richiamo la funzione
        x_circleSpeed = -x_circleSpeed #rimbalzo della pallina
        scoreLeft = scoreLeft+1 #aumento il punteggio del giocatore sinistro
        
    if ( x_Circle < 0 + circleWidth/2):#se la x della pallina supera la larghezza totale
        setup()#richiamo la funzione 
        x_circleSpeed = -x_circleSpeed #rimbalzo della pallina
        scoreRight = scoreRight+1 #aumento il punteggio del giocatore destro
        
    if ( y_Circle > totalHeigth - circleHeight/2 ):#se la y della pallina supera la altezza totale
        y_circleSpeed = -y_circleSpeed #rimbalzo della pallina
        
    if ( y_Circle < 0 + circleHeight/2):#se la y della pallina supera la altezza totale
        y_circleSpeed = -y_circleSpeed #rimbalzo della pallina

        
def keyPressed():
    global y_paddleLeft, y_paddleRight, y_paddleSpacepeed
    if (key== "w" or key=="W"): #premendo w o W la racchetta sinistra si muoverà verso l'alto
        y_paddleLeft -=y_paddleSpacepeed #modifico la y diminuendola , cosi da far muovere la racchetta verso l'alto
    
    if (key == "z" or key =="Z"): #premendo z o Z la racchetta sinistra si muoverà verso il basso
        y_paddleLeft +=y_paddleSpacepeed #modifico la y aumentandola , cosi da far muovere la racchetta verso il basso
   
    if (keyCode == DOWN): #premendo la freccetta in basso la racchetta destra va in basso
        y_paddleRight +=y_paddleSpacepeed #modifico la y aumentandola , cosi da far muovere la racchetta verso il basso
    
    if (keyCode== UP): #premendo la freccetta in alto la racchetta destra va in alto
        y_paddleRight -=y_paddleSpacepeed # modifico la y diminiuendola, cosi da far muovere la racchetta verso l'alto

def contactPaddle():
    global x_Circle,x_paddleRight,paddleWidth,x_circleSpeed,y_circleSpeed,y_paddleLeft, circleHeight,circleWidth,y_Circle,y_paddleRight,x_paddleLeft
    if(x_Circle - circleWidth/2 < x_paddleLeft + paddleWidth/2 and y_Circle - circleHeight/2 < y_paddleLeft +paddleHeigth/2 and  y_Circle + circleHeight/2 > y_paddleLeft-paddleHeigth/2):#controllo per far rimbalzare la pallina al contatto con la racchetta sinistra
        if(x_circleSpeed < 0): # se variabile velocita pallina coordinata x < 0
            x_circleSpeed = -x_circleSpeed #rimbalzo della pallina al contatto con la racchetta
    
    if(x_Circle + circleWidth/2 > x_paddleRight - paddleWidth/2 and y_Circle - circleHeight/2 < y_paddleRight +paddleHeigth/2 and  y_Circle + circleHeight/2 > y_paddleRight-paddleHeigth/2):#controllo per far rimbalzare la pallina al contatto con la racchetta destra
        if(x_circleSpeed > 0): # se variabile velocita pallina coordinata x > 0
            x_circleSpeed = -x_circleSpeed #rimbalzo della pallina al contatto con la racchetta
        
def restrictPaddle():
    global y_paddleLeft, paddleHeigth, paddleSpace, y_paddleRight
    if(y_paddleLeft - paddleHeigth/2 < 0): #controllo quando la pallina tocca lo spigolo della racchetta sinistra
        y_paddleLeft = y_paddleLeft + paddleSpace
    
    if(y_paddleLeft + paddleHeigth/2 > height):
        y_paddleLeft = y_paddleLeft - paddleSpace
        
    if(y_paddleRight - paddleHeigth/2 < 0): #controllo quando la pallina tocca lo spigolo della racchetta destra
        y_paddleRight = y_paddleRight + paddleSpace
        
    if(y_paddleRight + paddleHeigth/2 > height):
        y_paddleRight = y_paddleRight - paddleSpace    
        
def scores():
    global scoreLeft, scoreRight, winScore
    fill(255); #colore bianco per i punti
    text(scoreLeft, 320, 30) #viene scritto e posizionato il punteggio del giocatore sinistro
    text(scoreRight, 367, 30) #viene scritto e posizionato il punteggio del giocatore destro    

def gameOver():
    global scoreLeft, scoreRight, winScore, colorL, colorR, x_circleSpeed, y_circleSpeed
    if(scoreLeft==winScore): #se il punteggio del giocatore sinistro è uguale alla variabile che conta il punteggio massimo che si puo raggiungere
        fill(255,0,0) #colore rosso 
        text("RED WIN", 110, 110) #viene scritta e posizionata la frase RED WIN
        x_circleSpeed=0 #far fermare la pallina poiche il gioco è terminato, quindi riportare la pallina a coordinata x=0
        y_circleSpeed=0 #far fermare la pallina poiche il gioco è terminato, quindi riportare la pallina a coordinata y=0
    
    if(scoreRight==winScore): #se il punteggio del giocatore destro è uguale alla variabile che conta il punteggio massimo che si puo raggiungere
        fill(0,0,255) #colore blu
        text("BLU WIN", 495 , 390) #viene scritta e posizionata la frase BLU WIN
        x_circleSpeed=0 #far fermare la pallina poiche il gioco è terminato, quindi riportare la pallina a coordinata x=0
        y_circleSpeed=0 #far fermare la pallina poiche il gioco è terminato, quindi riportare la pallina a coordinata y=0
