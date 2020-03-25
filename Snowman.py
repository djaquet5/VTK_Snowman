"""
Lab: 1-Snowman
Authors: David Jaquet, Luc Wachter
Description: Reproduce the video at the following link using VTK and its python wrapper
             https://youtu.be/hthbXe_boXc
Python version: 3.7.4
"""

import vtk
import time


# Generate an actor with a sphere shape
def getSphereActor(pos, radius):
    sphere = vtk.vtkSphereSource()
    sphere.SetCenter(pos[0], pos[1], pos[2])
    sphere.SetRadius(radius)
    sphere.SetPhiResolution(50)
    sphere.SetThetaResolution(50)

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(sphere.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    return actor


head = getSphereActor([-20, 0, 0], 8)
body = getSphereActor([0, 0, 0], 10)

# Nose
nose = vtk.vtkConeSource()
nose.SetDirection(0, -90, 0)
nose.SetCenter(28, 0, 0)
nose.SetHeight(3.0)
nose.SetRadius(1.0)
nose.SetResolution(50)

noseMapper = vtk.vtkPolyDataMapper()
noseMapper.SetInputConnection(nose.GetOutputPort())

noseActor = vtk.vtkActor()
noseActor.SetMapper(noseMapper)
noseActor.GetProperty().SetColor(0.925, 0.65, 0)

# Renderer
renderer = vtk.vtkRenderer()
renderer.AddActor(head)
renderer.AddActor(body)
renderer.AddActor(noseActor)

# Color picked from the demo video
renderer.SetBackground(1, 0.894, 0.898)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(renderer)
renWin.SetSize(600, 600)


def displayLoop(rangeEnd, displayFunc, value):
    for i in range(0, rangeEnd):
        time.sleep(0.03)

        renWin.Render()
        displayFunc(value)


# Align the head with the body
displayLoop(180, head.RotateZ, -0.5)

# Put the head on the body
# TODO: Use display loop ?
for i in range(0, 30):
    time.sleep(0.03)

    renWin.Render()

    position = head.GetPosition()
    head.SetPosition(position[0], position[1]-0.1, position[2])

# TODO: Align the nose with the body
# FIXME: Edit range, the nose disapear in front of camera
# displayLoop(1000, noseActor.RotateY, -0.5)

# TODO: The nose should be inside the head
for i in range(0, 180):
    time.sleep(0.03)

    renWin.Render()

    position = noseActor.GetPosition()
    noseActor.SetPosition(position[0], position[1]+0.1, position[2])
    noseActor.RotateX(-0.4)

# FIXME: edit interval and increment
# Pull out the nose
# for i in range(0, 30):
#     time.sleep(0.03)
#
#     renWin.Render()
#
#     position = noseActor.GetPosition()
#     noseActor.SetPosition(position[0], position[1], position[2]+1)

# Eyes
leftEye = getSphereActor([-2, 18, 7], 1.5)
leftEye.GetProperty().SetColor(0, 0, 0)

rightEye = getSphereActor([2, 18, 7], 1.5)
rightEye.GetProperty().SetColor(0, 0, 0)

renderer.AddActor(leftEye)
renderer.AddActor(rightEye)
renWin.Render()

# Roll the camera
displayLoop(360, renderer.GetActiveCamera().Roll, 1)

# Traveling around the snowman
displayLoop(360, renderer.GetActiveCamera().Azimuth, 1)

# Lift the camera to see the snowman from above
displayLoop(80, renderer.GetActiveCamera().Elevation, 1)

# Lower the camera to have the snowman in front of the camera
displayLoop(80, renderer.GetActiveCamera().Elevation, -1)
