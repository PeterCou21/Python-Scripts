from vpython import *
#GlowScript 2.7 VPython
#sections for constants
mass_size = vec(1,1,1)
mass_mass = 1
ip = 1
ap = -1
color.lblue = vec(0, 255, 237)

#initial displacement magnitude
dis_mag = 2
#this is the mode selection: Type 'ip' for the masses to be in phase or type 'ap' for the masses to be 'anti-phase'
mode_sel = ip


#this is the code for the display, it should be 600 pixels wide and high and should be white################################################
display(width = 600, height = 600, 
        center = vec(6,0,0), 
        background = color.white)
# this is where the graph is defined        
graph1= graph(xmin = 0, xmax = 30, 
              ymin = 0, ymax = 15,
              title = 'Displacement as a function of time',
              xtitle = 'time(s)',
              ytitle = 'displacement(m)',
              height = 300,
              width = 600,
              align = 'left')

############this is the code for the objects that are displayed in the code################################################################

base = box(size = vec(21,0.2,4), pos = vec(7,-0.6,0), texture = "https://i.imgur.com/cKQopaa.png")
wall = box(size = vec(0.2,3,2), pos = vec(0,1,0), texture = "https://i.imgur.com/cKQopaa.png")
wall2 = box(size = vec(0.2,3,2), pos = vec(15,1,0), texture = "https://i.imgur.com/cKQopaa.png")
mass = box(size = mass_size, pos = vec(3,0,0), velocity = vec(0,0,0), mass = mass_mass, color= color.blue)
mass2 = box(size = mass_size, pos = vec(12,0,0), velocity = vec(0,0,0), mass = mass_mass, color = color.blue)


#This is where pivot points are defined for the spring#####################################################################################
pivot = vector(0,0,0)
pivot2 = vector(15,0,0)

##############This is where the springs are created and defined############################################################################

spring = helix(pos = pivot, axis = mass.pos - pivot, radius = 0.4, thickness = 0.1, coils = 20, constant = 1, color = color.lblue)
spring2 = helix(pos = pivot2, axis = mass2.pos - pivot2 , radius = 0.4, thickness = 0.1, coils = 20, constant = 1, color = color.lblue)
spring3 = helix(pos = vec(wall.pos.x,0,0), axis = vec(mass2.pos.x-wall2.pos.x,0,0), radius = 0.4, thickness = 0.1, coils = 20, constant = 1, color = color.lblue)
#########################
mass_dis_1 = gcurve(graph=graph1, color = color.black)
mass_dis_2 = gcurve(graph=graph1, color = color.green)


#########################
t=0
dt = 0.01
eqb = mass.pos
eqb2 = mass2.pos

mass.pos += vec(dis_mag*mode_sel,0,0)
mass2.pos += vec(dis_mag,0,0)
###########################################################################################################################################


while t < 3e4:
    rate(1000)   
#####acceleration, velocity, force and displacement calculation###########################################################################
    acc1 = (-(spring.constant+spring2.constant) * (mass.pos-eqb) + spring2.constant*(mass2.pos-eqb2))/mass.mass   
    vel = mass.velocity + acc1 * dt
    dis = mass.pos + vel * dt
    
    acc2 = (1*(mass.pos-eqb) - (spring2.constant+1) * (mass2.pos-eqb2))/mass2.mass
    vel2 = mass2.velocity + acc2 * dt
    dis2 = mass2.pos + vel2 * dt
    
############spring position#########################################################################################################################
    spring.axis = mass.pos - pivot
    spring2.axis = mass2.pos - pivot2
    spring3.axis = vec(mass2.pos.x-mass.pos.x,0,0)
    spring3.pos = vec(mass.pos.x,0,0)
    # assigning calculation to objects
    mass.velocity = vel
    mass.pos = dis
    
    mass2.velocity = vel2
    mass2.pos = dis2
    
    # plot being plotted 
    mass_dis_1.plot(t, mass.pos.x)
    mass_dis_2.plot(t, mass2.pos.x)   
    t += dt
