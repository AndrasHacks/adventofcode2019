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

def get_orbit_count(dict_map, source, dest = 'COM', count = 0):
    if source == dest:
        return count
    else:
        centers = dict_map[source]
        for center in centers:
            return  get_orbit_count(dict_map, center, dest, count + 1)

def get_route(dict_map, source, dest, route = None):
    if route == None:
        route = []
        route.append(source)
    if source == dest:
        return route
    else:
        centers = dict_map[source]
        for center in centers:
            route.append(center)
            return get_route(dict_map, center, dest, route)

def get_check_sum(dict_map):
    count = 0
    for planet in dict_map.keys():
        count += get_orbit_count(dict_map, planet)
    return count
