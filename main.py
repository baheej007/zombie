import pygame as pg 
screen=pg.display.set_mode(( 500,800))
while True:
  for ev in pg.event.get():
    if ev.type==pg.MOUSEBUTTONDOWN:
      pos = pg.mouse.get_pos()
      col = (0,255,255)
      pg.draw.rect(screen,col,pg.Rect(pos, (80,50))) 
      pg.display.update() 
    if ev.type==pg.MOUSEBUTTONUP:
      pos = pg.mouse.get_pos()
      col = (0,255,255)
      pg.draw.circle(screen,col,pos,20,5)
      pg.display.update()