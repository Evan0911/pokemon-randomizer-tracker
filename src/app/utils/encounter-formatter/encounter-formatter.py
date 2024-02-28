from enum import Enum
import json
import traceback
import os

script_dir = os.path.dirname(__file__)
file = open(script_dir + '/encounter-emerald.txt')
lines = file.readlines()
methods = Enum('methods', ['fish', 'surf', 'dive', 'walk', 'rockSmash'])
rods = Enum('rods', ['old', 'good', 'super', 'none'])
method = methods.walk
rod = rods.old

def formatWithNames():
    try:
        index = 0
        output = []
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
                                if (method.name not in output[index-1]):
                                    output[index-1][method.name] = {}
                                    
                                if(rod == rods.none):
                                    if (output[index-1][method.name] == {}):
                                        output[index-1][method.name] = {rods.old.name: [pokemon], rods.good.name: [pokemon], rods.super.name: [pokemon]}
                                    else:
                                        output[index-1][method.name][rods.old.name] = [pokemon]
                                        output[index-1][method.name][rods.good.name] = [pokemon]
                                        output[index-1][method.name][rods.super.name] = [pokemon]
                                else:
                                    if (rod.name not in output[index-1][method.name]):
                                        output[index-1][method.name][rod.name] = [pokemon]
                                    else:
                                        output[index-1][method.name][rod.name].append(pokemon)
                            else:
                                if (method.name not in output[index-1]):
                                    output[index-1][method.name] = [pokemon]
                                else:
                                    output[index-1][method.name].append(pokemon)
                else:
                    index += 1
                    output.append({"zone": line.strip().replace('\n', '')})
                    method = methods.walk
                    rod = rods.none
        open(script_dir + '/encounter-emerald.json', 'w').write(json.dumps(output, indent=4))
    except Exception as e:
        print(index, '\n', output[index-1], '\n', pokemon, '\n', method.name, '\n', rod.name, '\n', traceback.format_exc())

def formatWithoutNames():
    try:
        index = 0
        output = []
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
                            if(method == methods.fish):
                                if (method.name not in output[index-1]):
                                    output[index-1][method.name] = {}
                                    
                                if(rod == rods.none):
                                    if (output[index-1][method.name] == {}):
                                        output[index-1][method.name] = {rods.old.name: ["-"], rods.good.name: ["-"], rods.super.name: ["-"]}
                                    else:
                                        output[index-1][method.name][rods.old.name] = ["-"]
                                        output[index-1][method.name][rods.good.name] = ["-"]
                                        output[index-1][method.name][rods.super.name] = ["-"]
                                else:
                                    if (rod.name not in output[index-1][method.name]):
                                        output[index-1][method.name][rod.name] = ["-"]
                                    else:
                                        output[index-1][method.name][rod.name].append("-")
                            else:
                                if (method.name not in output[index-1]):
                                    output[index-1][method.name] = ["-"]
                                else:
                                    output[index-1][method.name].append("-")
                else:
                    index += 1
                    output.append({"zone": line.strip().replace('\n', '')})
                    method = methods.walk
                    rod = rods.none
        open(script_dir + '/encounter-emerald-without-name.json', 'w').write(json.dumps(output, indent=4))
    except Exception as e:
        print(index, '\n', output[index-1], '\n', method.name, '\n', rod.name, '\n', traceback.format_exc())

formatWithNames()
formatWithoutNames()