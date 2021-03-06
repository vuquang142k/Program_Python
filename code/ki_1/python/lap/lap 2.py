x, y = map(float, input('Введите координат: ').split(' '))

ok=False
if (1 <= x <= 9 and y <= (-1/8)*(x-9)**2+8):
    if (y >= (1/49)*(x-1)**2 and 1 <= x <= 8) or (y >= 7*(x-8)**2+1 and 8 <= x <= 9):
            ok=True
            
if (-9 <= x <= -1 and y <= (-1/8)*(x+9)**2+8):
    if (y >= (1/49)*(x+1)**2 and -8 <= x <= -1) or (y >= 7*(x+8)**2+1 and -9 <= x <= -8):
            ok=True
                
if (2 <= x <= 8 and y >= (1/3)*(x-5)**2-7) or (1 <= x <= 2 and y >= 2*(x-1)**2-2):
    if 1 <= x <= 8 and y <= (-4/49)*(x-1)**2:
        ok=True
               
if (-8 <= x <= -2 and y >= (1/3)*(x+5)**2-7) or (-2 <= x <= -1 and y >= 2*(x+1)**2-2):
    if -8 <= x <= -1 and y <= (-4/49)*(x+1)**2:
        ok=True
  
        
        
if -1 <= x <= 1 and y <=-4*x**2+2:
    if -1 <= x <= 1 and y >= 4*x**2-6:
        ok=True
            
if 0 <= abs(x) <= 2 and y == (3/2)*x+2:
    ok=True
    
if ok:
    print('Точка принадлежает в бабочке')
else:
    print('Точка не принадлежает в бабочке')

        
    
