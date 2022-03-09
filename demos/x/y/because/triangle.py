#definition of a function - specifying what it is and what it does
def calc_area(h=8 , b=1):
    area = 0.5*h*b 
    return area   
#return value = data produced by function and given back to the caller
  
def run():  
  #call to the function to run 
  total_area = calc_area(2, 10) + calc_area(9) + calc_area() +     calc_area(b=10)


  print(f"The are is {total_area} cm^2")
