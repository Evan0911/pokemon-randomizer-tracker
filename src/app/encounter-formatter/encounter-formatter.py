from enum import Enum
import json
import traceback

file = open('utils/encounter-formatter/encounter-emerald.txt')
lines = file.readlines()
output = {}
methods = Enum('methods', ['fish', 'surf', 'dive', 'walk', 'rockSmash'])
rods = Enum('rods', ['old', 'good', 'super', 'none'])
method = methods.walk
rod = rods.old
route = ''

try:
    for line in lines:
        if (line.strip()):
            if line.startswith(' '):
                key = line.strip().replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '')
                match key:
                    case 'fish':
                        method = methods.fish
                    case 'surf':
                        method = methods.surf
                    case 'underwater':
                        method = methods.dive
                    case 'rock smash':
                        method = methods.rockSmash
                    case 'OldRod':
                        rod = rods.old
                    case 'GoodRod':
                        rod = rods.good
                    case 'SuperRod':
                        rod = rods.super
                    case _:
                        pokemon = key.split('Lv')[0]
                        if(method == methods.fish):
                            if (method.name not in output[route]):
                                output[route][method.name] = {}
                                
                            if(rod == rods.none):
                                if (output[route][method.name] == {}):
                                    output[route][method.name] = {rods.old.name: [pokemon], rods.good.name: [pokemon], rods.super.name: [pokemon]}
                                else:
                                    output[route][method.name][rods.old.name] = [pokemon]
                                    output[route][method.name][rods.good.name] = [pokemon]
                                    output[route][method.name][rods.super.name] = [pokemon]
                            else:
                                if (rod.name not in output[route][method.name]):
                                    output[route][method.name][rod.name] = [pokemon]
                                else:
                                    output[route][method.name][rod.name].append(pokemon)
                        else:
                            if (method.name not in output[route]):
                                output[route][method.name] = [pokemon]
                            else:
                                output[route][method.name].append(pokemon)
            else:
                route = line.strip().replace('\n', '')
                output[route] = {}
                method = methods.walk
                rod = rods.none
except Exception as e:
    print(route, '\n', output[route], '\n', pokemon, '\n', method.name, '\n', rod.name, '\n', traceback.format_exc())

open('utils/encounter-formatter/encounter-emerald.json', 'w').write(json.dumps(output, indent=4))