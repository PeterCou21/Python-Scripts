from vpython import *
#GlowScript 2.7 VPython
#sections for constants
mass_size = vec(1,1,1)
mass_mass = 1
floor = 30
color.yeet = vec(0, 255, 237)
#mode selection: '0' stationary, 1 for mode 1, 2 for mode 2 and 3 for mode 3#
mode_select = 3

#inital displacement magnitude
mag_of_displacement = 1
mode_type = [[0,1,1,1],[0,sqrt(2),0,-sqrt(2)],[0,1,-1,1]]
    
    
#this is the code for the display, it should be 600 pixels wide and high and should be white################################################
display(width = 600, height = 600, 
        center = vec(6,0,0), 
        background = color.white)
####This is where the graph is defined#########################################################################################################################        
graph1= graph(xmin = 0, xmax = 30, 
              ymin = 0, ymax = 30,
              title = 'Displacement as a function of time',
              xtitle = 'time(s)',
              ytitle = 'displacement(m)',
              height = 300,
              width = 600,
              align = 'left')

############This is the code for the objects that are displayed in the code, such as the masses and walls################################################################

base = box(size = vec(floor,0.2,4), pos = vec(12,-0.6,0), texture = "https://i.imgur.com/cKQopaa.png")

wall = box(size = vec(0.2,3,2), pos = vec(0,1,0), texture = "https://i.imgur.com/cKQopaa.png")

wall2 = box(size = vec(0.2,3,2), pos = vec(24,1,0), texture = "https://i.imgur.com/cKQopaa.png")

mass = box(size = mass_size, pos = vec(6,0,0), velocity = vec(0,0,0), mass = mass_mass, color= color.red)

mass2 = box(size = mass_size, pos = vec(18,0,0), velocity = vec(0,0,0), mass = mass_mass, color = color.blue)

##################################new mass(the mass in the centre 'm3')########################################################################################
mass3 = box(size = mass_size, pos = vec(12,0,0), velocity = vec(0,0,0), mass = mass_mass, color = color.green)

#This is where 'pivot' points are defined for the spring#####################################################################################
pivot = vector(0,0,0)
pivot2 = vector(24,0,0)

##############This is where the springs are created and defined############################################################################

spring = helix(pos = pivot,
                axis = mass.pos - pivot,
                radius = 0.4,
                thickness = 0.1,
                coils = 20,
                constant = 1,
                color = color.yeet
                )
                
spring2 = helix(pos = pivot2,
                axis = mass2.pos - pivot2,
                radius = 0.4,
                thickness = 0.1,
                coils = 20,
                constant = 1,
                color = color.yeet
                )

####new left spring (attached to Mass1 and Mass3 )##########################################################################################################################################
spring3 = helix(pos = vec(mass.pos.x,0,0),
                axis = vec(mass2.pos.x-mass.pos.x,0,0),
                radius = 0.4,
                thickness = 0.1,
                coils = 20,
                constant = 1,
                color = color.red
                )

######new right spring(attached to Mass3 and Mass 2)#####################################################################################################################################
spring4 = helix(pos = vec(mass3.pos.x,0,0),
                axis = vec(-(mass3.pos.x-mass2.pos.x),0,0),
                radius = 0.4,
                thickness = 0.1,
                coils = 20,
                constant = 1,
                color = color.black
                )

#######graphs for mass displacement##########################################################################################################################

mass_dis_1 = gcurve(graph=graph1, color = color.red)
mass_dis_2 = gcurve(graph=graph1, color = color.blue)
mass_dis_3 = gcurve(graph=graph1, color = color.green)

#######time contants###########################################################################################################################################
t=0
dt = 0.01

###############equblibrium points################################################################################################################
eqb = vec(6,0,0)
eqb3 = vec(12,0,0)
eqb2 = vec(18,0,0)

#########################mass positions ###############################################################################
mass.pos += vec(mag_of_displacement*mode_type[0][mode_select],0,0)
mass2.pos += vec(mag_of_displacement*mode_type[2][mode_select],0,0)
mass3.pos += vec(mag_of_displacement*mode_type[1][mode_select],0,0)
###########################################################################################################################################

while t < 3e4:
    rate(1000)   
#####acceleration, velocity, force and displacement calcualations###########################################################################

 
    acc1 = (-(spring.constant+spring3.constant) * (mass.pos-eqb) + spring3.constant*(mass3.pos-eqb3))/mass.mass   
    vel = mass.velocity + acc1 * dt
    dis = mass.pos + vel * dt
    
    acc2 =  spring4.constant*(mass3.pos-eqb3) - (spring4.constant+spring3.constant) * (mass2.pos-eqb2)/mass2.mass
    vel2 = mass2.velocity + acc2 * dt
    dis2 = mass2.pos + vel2 * dt
    
####mass3 calculations for acceleration, velocity and displacement########################################################################
    acc3 = spring3.constant*(mass.pos-eqb) - ((spring3.constant+spring4.constant)*(mass3.pos - eqb3)) + (spring4.constant)*(mass2.pos - eqb2)/mass3.mass                     
    vel3 = mass3.velocity + acc3 * dt
    dis3 = mass3.pos + vel3 * dt
    
############spring axises#########################################################################################################################
    spring.axis = vec(-(wall.pos.x-mass.pos.x),0,0)
    spring2.axis = vec(mass2.pos.x-wall2.pos.x,0,0)
    ###################################

    ####new left spring axis and position######
    spring3.axis = vec(mass3.pos.x-mass.pos.x,0,0)
    spring3.pos = vec(mass.pos.x,0,0)
    ####new right spring axis and position####
    spring4.axis = vec(-(mass3.pos.x-mass2.pos.x),0,0) 
    spring4.pos = vec(mass3.pos.x,0,0)
    
######assigning the calculations to objects#########################################################################################################
    mass.velocity = vel
    mass.pos = dis
    
    mass2.velocity = vel2
    mass2.pos = dis2
    
    mass3.velocity = vel3
    mass3.pos = dis3
    
    # graphs being plotted # 
    mass_dis_1.plot(t, mass.pos.x)
    mass_dis_2.plot(t, mass2.pos.x)
    mass_dis_3.plot(t, mass3.pos.x)  
    t += dt
