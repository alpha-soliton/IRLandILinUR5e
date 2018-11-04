import pybullet as p
import time,math
import numpy as np

p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_RENDERING,0)
ur5e = p.loadURDF("data/ur_description/urdf/ur5_robot.urdf", [-2,3,-1.5], useFixedBase=1)
for i in range (p.getNumJoints(ur5e)):
	p.setJointMotorControl2(ur5e,i,p.POSITION_CONTROL,0)
	print(p.getJointInfo(ur5e,i))
print("check the joint id!")
key = input("press enter to start simulation")

if 1:
	objs = p.loadSDF("botlab/botlab.sdf", globalScaling=2.0)
	zero=[0,0,0]
	p.configureDebugVisualizer(p.COV_ENABLE_RENDERING,1)
	print("converting y to z axis")
	for o in objs:
		pos,orn = p.getBasePositionAndOrientation(o)
		y2x = p.getQuaternionFromEuler([3.14/2.,0,3.14/2])
		newpos,neworn = p.multiplyTransforms(zero,y2x,pos,orn)
		p.resetBasePositionAndOrientation(o,newpos,neworn)
else:
	p.loadURDF("plane.urdf",[0,0,-3])
	
p.loadURDF("boston_box.urdf",[-2,3,-2], useFixedBase=True)

p.resetDebugVisualizerCamera( cameraDistance=1, cameraYaw=148, cameraPitch=-9, cameraTargetPosition=[0.36,5.3,-0.62])

p.loadURDF("boston_box.urdf",[0,3,-2],useFixedBase=True)

p.configureDebugVisualizer(p.COV_ENABLE_RENDERING,1)

p.getCameraImage(320,200)#, renderer=p.ER_BULLET_HARDWARE_OPENGL )


t=0
p.setRealTimeSimulation(1)
while (1):
	p.setGravity(0,0,-10)
	time.sleep(0.01)
	t+=0.01
	keys = p.getKeyboardEvents()
	targ_angle = (t)
	p.setJointMotorControl2(ur5e,1,p.POSITION_CONTROL,-np.pi/4.)
	p.setJointMotorControl2(ur5e,4,p.POSITION_CONTROL,t)
	print(p.getJointInfo(ur5e,5))
	for k in keys:
		if (keys[k]&p.KEY_WAS_TRIGGERED):
			if (k == ord('i')):
				x = 10.*math.sin(t)
				y = 10.*math.cos(t)
				p.getCameraImage(320,200,lightDirection=[x,y,10],shadow=1)#, renderer=p.ER_BULLET_HARDWARE_OPENGL )
		
	
