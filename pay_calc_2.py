hrs = input('Enter hours: ')
rate = input('Enter rate: ')
try:
    r = int(rate) 
    h = int(hrs)
except: print('Please enter numeric values')

def computepay() :
    try:
        if  h > 40:
            pay = ((h - 40) * (r * 1.5)) + (r * 40)
            print(pay)
        else:
            pay = h * r
            print(pay)
    except:
        print('Please Enter Numeric Values')

computepay()
# except: print('Error: Please enter numeric value')