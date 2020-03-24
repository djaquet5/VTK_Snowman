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
def getSphereActor(posX, radius):
    sphere = vtk.vtkSphereSource()
    sphere.SetCenter(posX, 0, 0)
    sphere.SetRadius(radius)
    sphere.SetPhiResolution(50)
    sphere.SetThetaResolution(50)

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(sphere.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    return actor


head = getSphereActor(-20, 8)
body = getSphereActor(0, 10)

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

# Align the head with the body
for i in range(0, 180):
    time.sleep(0.03)

    renWin.Render()
    head.RotateZ(-0.5)

# Put the head on the body
for i in range(0, 30):
    time.sleep(0.03)

    renWin.Render()

    position = head.GetPosition()
    head.SetPosition(position[0], position[1]-0.1, position[2])

# TODO: Align the nose with the body
# FIXME: Edit range, the nose disapear in front of camera
# for i in range(0, 1000):
#     time.sleep(0.03)
#
#     renWin.Render()
#     noseActor.RotateY(-0.5)

# TODO: Lift the nose (with Pitch ?)

# TODO: Display nose and eyes

# Roll the camera
# TODO: Check if the lap is completed
for i in range(0, 360):
    time.sleep(0.03)

    renWin.Render()
    renderer.GetActiveCamera().Roll(1)

# Traveling around the snowman
# TODO: Check if the lap is completed
for i in range(0, 360):
    time.sleep(0.03)

    renWin.Render()
    renderer.GetActiveCamera().Azimuth(1)

# Lift the camera to see the snowman from above
for i in range(0, 80):
    time.sleep(0.03)

    renWin.Render()
    renderer.GetActiveCamera().Elevation(1)

# Lower the camera to have the snowman in front of the camera
for i in range(0, 80):
    time.sleep(0.03)

    renWin.Render()
    renderer.GetActiveCamera().Elevation(-1)
