def city_country(city,country,population=''):
    if population:
        full_cc =city +','+country+'-'+str(population)
    else:
        full_cc = city+','+country
    return full_cc.title()