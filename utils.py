import pycountry


def ukhomenation():
    prov = ()
    provincelist = list(pycountry.subdivisions.get(country_code='GB'))
    a = ('',)
    for p in provincelist:
        try:
            a = (p.parent.code,p.parent.name)
            prov += ((a),)
        except AttributeError:
            break
    prov = set(prov)
    prov = tuple(prov)
    return (prov)


def getcountry():
    countries_list = ()
    ukhn = ukhomenation()
    for country in pycountry.countries:
        countries_list += ((country.alpha_2, country.name),)
    countries_list += ukhn
    countries_list = tuple(sorted(countries_list, key=lambda country:country[1]))

    return countries_list


 
 
