from math import sin, cos, e

#Método da Secante

def secante(x0,x1,f,erro):

	f = eval('lambda x:' + f)
	
	it = 0
	
	print('Estimativas iniciais: x0 = {0}; x1 = {1} \n'.format(x0,x1))
	
	while(1):
		it+=1
		x = (x0*f(x1) - x1*f(x0))/(f(x1) - f(x0))
		
		e = abs(x-x1)/abs(x)  # erro
		
		print('it={0:d}  x={1:f} f(x)={2:f}  erro={3:e}'.format(it,x,f(x),e))
		
		x0 = x1
		x1 = x
		
		if(e <= erro):
			break
			
	print('Solução obtida: x = {0:.10f}'.format(x))
		
	return x	

f = '(7 * sin(x) * (e ** (x * -1))) - 1'

secante(0, 0.1, f, 0.0001)   