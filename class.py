import pygame
import math
import sys 
pygame.init()
yellow = (255,255,0)
White= (255,255,255)
blue=(100,149,237)
red=(188,39,50)
dark_grey=(80,78,81)
width, height= 800,800
lsitdist=[]
Font = pygame.font.SysFont('comicsans',16)
win=pygame.display.set_mode((width,height))
pygame.display.set_caption('planet simulation')
class planet:
  AU = 149.6e6*1000
  G = 6.67428e-11
  SCALE= 200/AU 
  TIMESTEP = 3600 *24 
  def __init__(self,x,y,radius,mass,color):
    self.mass= mass
    self.x= x 
    self.y= y
    self.radius=radius
    self.color=color
    
    self.sun = False
    self.orbit=[]
    self.distance_to_sun=0
    
    self.x_vel=0
    self.y_vel=0
  def draw(self,win):
    x =self.x*self.SCALE+ (width/2)
    y =self.y*self.SCALE+ (height/2)
    if len(self.orbit)>2:
       updated_points=[]
       for points in self.orbit:
         x,y =points 
         x= x*self.SCALE + width/2
         y= y*self.SCALE + height/2
         updated_points.append((x,y))

       pygame.draw.lines(win,self.color,False,updated_points,2)
    if not self.sun:
      text = Font.render(f'{round(self.distance_to_sun/1000)}Km',1,White)
      win.blit(text,((x - text.get_width()/2),(y-text.get_height()/2)))
    pygame.draw.circle(win,self.color,(x,y),self.radius)
    
  def force(self,other):
    other_x,other_y= other.x,other.y
    distance_x= other.x-self.x
    distance_y = other.y-self.y
    distance =  math.sqrt((distance_x**2)+ (distance_y**2))
    if other.sun:
      self.distance_to_sun = distance
      lsitdist.append(self.distance_to_sun)
    Force= (self.G* self.mass* other.mass)/ distance**2
    theta = math.atan2(distance_y,distance_x)
    Force_x= math.cos(theta) * Force
    Force_y = math.sin(theta)* Force
    return Force_x, Force_y
  def update_position(self, Planets):
    total_fx=0
    total_fy=0
    for i in Planets:
      if self== i:
        continue
      fx, fy= self.force(i)
      total_fx+= fx
      total_fy+=fy 

    self.x_vel += (total_fx/self.mass) * self.TIMESTEP
    self.y_vel += total_fy/self.mass * self.TIMESTEP
    self.x+= self.x_vel * self.TIMESTEP
    self.y+= self.y_vel* self.TIMESTEP
    self.orbit.append((self.x,self.y))
  def distancefromsun(self,sun):
     max_value = lsitdist[0]
     for num in lsitdist:
        if max_value is None or num > max_value:
            max_value = num
     return max_value
def main():
  run = True 
  clock = pygame.time.Clock()
  sun = planet(0,0,30,1.98892*10**30,yellow)
  earth =planet(-1*planet.AU,0,16,5.9742*10**24,blue)
  earth.y_vel = 29.783*1000
  mars = planet(-1.524*planet.AU,0,12,6.39*10**23,red)
  mars.y_vel= 24.077*1000
  mercury= planet(0.387*planet.AU,0,8,3.30*10**23,dark_grey)
  mercury.y_vel= -47.4*1000
  venus = planet(0.723*planet.AU,0,14,4.8685*10**24,White)
  venus.y_vel= -35.02*1000

  sun.sun= True
  Planets=[sun,earth,venus,mars,mercury]
  while run:
     clock.tick(60)
     win.fill((0,0,0))
     for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
         run = False
     for i in Planets:
       i.update_position(Planets)
       i.draw(win)
    
     pygame.display.update()
     
  pygame.quit()
  sys.exit()
main()



 