def make_car(conductor,size,**information):
    information['conductor'] = conductor
    information['size'] = size
    for key,value in information.items():
        information[key] = value
    return information
car = make_car('subaru','outback',color='blue',tow_package=True)
print(car)