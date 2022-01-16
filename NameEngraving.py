#A short name engraving program by Muhammad Imran bin Ismael 1810633
from robolink import *    # RoboDK's API
from robodk import *      # Math toolbox for robots
import csv                # To import excel file


# Opening Excel Files
file = open("C:/Users/user/Documents/SEM 1 2122/Robotics/NameCoordinates.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)

# Converting the list of list into floats to ease of additions
rows = [list(map(float, sublist)) for sublist in rows]
print(rows) # For verification of floats type

# Start the RoboDK API:
RDK = Robolink()

# Get the robot (first robot found):
robot = RDK.Item('', ITEM_TYPE_ROBOT)

# Get the reference target by name:
target = RDK.Item('Target 1')
home=RDK.Item('Home')
target_pose = target.Pose()
xyz_ref = [target_pose.Pos()]
print(xyz_ref) # For verification of floats type
robot.MoveJ(home) # Move to Home position
robot.MoveJ(target) # Move to Target 1 position


# Start engraving name:MUHAMMAD IMRAN BIN ISMAEL
for i in range(2030): # 2030 as in the number of total coordinates
    # Calculate the new position:
    x = xyz_ref[0][0]+ (rows[i][0]/8)
    y = xyz_ref[0][1]+ (rows[i][1]/8)
    z = xyz_ref[0][2]
    target_pose.setPos([x,y,z])
    robot.MoveL(target_pose)

# Trigger a program call at the end of the movement
robot.RunInstruction('Program_Done')
 
