import turtle as t 
import colorsys
t.bgcolor("black")
t.speed(50)
color=('white','red')
for i in range(1000):
   t.color(color[i%2])
   t.fd(i)
   t.rt(45)
   t.circle(65,139)
   t.fd(150-i)
   t.backward(60)
t.done() 

    
    
   






    
    
    