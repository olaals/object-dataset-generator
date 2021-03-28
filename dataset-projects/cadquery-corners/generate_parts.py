import cadquery as cq
from random import uniform, randint
import random
import os
from cadquery import exporters

dataset_folder = 'dataset'
subfolder = 'stl-corners'
save_folder = os.path.join(dataset_folder, subfolder)


def hModule1(result,length):
    l2 = uniform(0,length)
    l3 = uniform(0,length-l2)
    l1 = length-l3-l2
    l4 = uniform(0,length/4)
    result = result.vLine(-l1)
    result = result.hLine(l4)
    result = result.vLine(-l2)
    result = result.hLine(-l4)
    result = result.vLine(-l3)
    return result

def hModule2(result, length):
    l1 = uniform(0,length)
    l2 = uniform(0,length-l1)
    l3 = length -l2-l1
    l4 = uniform(0,length/3)
    result = result.vLine(-l1)
    result = result.line(l4,-l2)
    result = result.vLine(-l3)
    return result

def hModule3(result, length):
    l1 = uniform(0,length)
    l2 = uniform(0,length-l1)
    l3 = length -l2-l1
    l4 = uniform(length/9,length/5)
    result = result.vLine(-l1)
    result = result.line(-l4,-l2)
    result = result.vLine(-l3)
    return result

def hModule4(result, length):
    l1 = length/3
    l2 = l1
    l3 = l1
    l4 = uniform(length/7,length/3)
    result = result.vLine(-l1)
    result = result.line(l4, l1)
    result = result.vLine(-l1-l2-l3)
    result = result.line(-l4, l3)
    result = result.vLine(-l3)
    return result

def hModule5(result, length):
    l1 = length/2
    l2 = l1
    l4 = uniform(0,length/3)
    result = result.vLine(-l1)
    result = result.hLine(l4)
    result = result.vLine(-l2)
    return result

def hModule6(result, length):
    l1 = length/2
    l2 = l1
    l4 = uniform(0,length/3)
    result = result.vLine(-l1)
    result = result.hLine(-l4)
    result = result.vLine(-l2)
    return result

def hModule7(result, length):
    l1 = length/3
    l2 = l1
    l3 = l1
    l4 = uniform(length/7,length/3)
    result = result.line(l4, -l1)
    result = result.vLine(-l2)
    result = result.line(-l4, -l3)
    return result

def hModule8(result, length):
    l8 = length/8
    l1 = 4*l8
    ld = uniform(length/5,length/4)
    result = result.vLine(-l8)
    result = result.hLine(ld)
    result = result.vLine(-l8)
    result = result.hLine(-ld)
    result = result.vLine(-l1)
    result = result.hLine(ld)
    result = result.vLine(-l8)
    result = result.hLine(-ld)
    result = result.vLine(-l8)
    return result

def hModule9(result, length):
    result = result.vLine(-length)
    return result
    
    

def cMod1(result, base_thickness):
    result = result.lineTo(base_thickness,base_thickness)
    l1 = uniform(-base_thickness/2, base_thickness/2)
    result = result.line(base_thickness, l1)
    result = result.moveTo(base_thickness, l1)
    return result

def cMod2(result, base_thickness):
    result = result.hLine(base_thickness/2)
    result = result.lineTo(base_thickness, 3/2*base_thickness)
    result = result.lineTo(base_thickness,base_thickness)
    result = result.hLine(base_thickness)
    return result

def cMod3(result, base_thickness):
    radius = uniform(0.2*base_thickness, 0.6*base_thickness)
    result = result.lineTo(base_thickness, radius*3)
    result = result.radiusArc((radius*3, base_thickness), 3/2*radius)
    result = result.moveTo(radius*3, base_thickness)
    return result

def cMod4(result, length):
    result=result.vLine(-length)
    result=result.hLine(length)
    return result

def vMod1(result, length):
    l1 = uniform(length*0.6, length*0.9)
    l2 = (length-l1)/2
    lh = uniform(length*0.2, length*0.4)
    result = result.hLine(l2)
    result = result.vLine(lh)
    result = result.hLine(l1)
    result = result.vLine(-lh)
    result = result.hLine(l2)
    return result

def vMod2(result, length):
    l1 = uniform(0,length)
    l2 = uniform(0,length-l1)
    l3 = length -l2-l1
    l4 = uniform(length/9,length/5)
    result = result.hLine(l1)
    result = result.vLine(-l4)
    result = result.hLine(l2)
    result = result.vLine(l3)
    return result

def vMod3(result, length):
    l2 = uniform(0,length)
    l1 = length-l2
    lh = uniform(length/4,length/3)
    result = result.line(l1,lh)
    result = result.line(l2,-lh)
    return result

def vMod4(result, length):
    result = result.hLine(length)
    return result
    
    


def create_base(result, H, L, base_thickness):
    result = result.moveTo(L,base_thickness)
    result = result.vLine(-base_thickness)
    result = result.hLine(-L)
    result = result.vLine(H)
    result = result.hLine(base_thickness)
    return result
    

def create_random_part(H,L,base_thickness, step, h_mods, c_mods, v_mods):
    result = cq.Workplane("XZ" )
    result = create_base(result, H,L,base_thickness)


    for i in range(5):
        ind = randint(0,len(h_mods)-1)
        result = h_mods[ind](result, step)

    result = random.choice(c_mods)(result, step)

    for i in range(5):
        result = random.choice(v_mods)(result,step)

    result = result.close().extrude(extrude).translate((0,extrude/2,0))
    return result




H = 1
L = 1
extrude = 1
step = 0.15
base_thickness = 0.1

h_mods = [hModule1, hModule2, hModule3, hModule4, hModule5, hModule6, hModule7, hModule8, hModule9]
c_mods = [cMod1, cMod2, cMod3, cMod4]
v_mods = [vMod1, vMod2, vMod3, vMod4]

number_of_parts = 500
filename = "mesh"
extension = ".stl"


for part_ind in range(number_of_parts):
    result = create_random_part(H,L,base_thickness, step, h_mods,c_mods,v_mods)
    export_path = os.path.join(save_folder, filename+('%03d' % part_ind)+extension)
    exporters.export(result, export_path)








