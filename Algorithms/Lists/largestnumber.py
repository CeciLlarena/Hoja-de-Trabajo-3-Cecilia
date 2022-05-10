def cuadrado(num): 
  result = num ** 2
  return result


def cubo(num): 
  result =num ** 3
  return result 

def f_to_c(temp_f):
  temp_c = (temp_f - 32) / 1.8
  return str(temp_c) + "C"



def c_to_f(temp_c): 
  temp_f = (1.8 * temp_c ) + 32
  return str(temp_f) + "F"

#import mate
#from temp import c_to_f, f_to_c

#result_1 = mate.cuadrado(16)
#print(result_1)

#result_2 = mate.cubo(16)
#print(result_2)

#result_3 = c_to_f(43)
#print(result_3)

#result_4 = f_to_c(100)
#print(result_4)