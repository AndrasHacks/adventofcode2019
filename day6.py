def get_dict(str_map):
    lines = str_map.split('\n')
    res_dict = {}
    for line in lines:
        planets = line.split(')')
        if len(planets) > 1:
            if planets[1] not in res_dict:
                res_dict[planets[1]] = []
                res_dict[planets[1]].append(planets[0])
            else:
                if planets[0] not in res_dict[planets[1]]:
                    res_dict[planets[1]].append(planets[0])
    return res_dict

def get_orbit_count(dict_map, planet, count = 0):
    if planet == 'COM':
        return count
    else:
        centers = dict_map[planet]
        for center in centers:
            return  get_orbit_count(dict_map, center, count + 1)

def get_check_sum(dict_map):
    count = 0
    for planet in dict_map.keys():
        count += get_orbit_count(dict_map, planet)
    return count
