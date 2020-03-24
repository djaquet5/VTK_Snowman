"""
Lab: 1-Snowman
Authors: David Jaquet, Luc Wachter
Description: Reproduce the video at the following link using VTK and its python wrapper
             https://youtu.be/hthbXe_boXc
Python version: 3.7.4
"""

import vtk
import time

# Head
head = vtk.vtkSphereSource()
head.SetCenter(0, 0, 0)
head.SetRadius(8.0)
head.SetThetaResolution(50)

headMapper = vtk.vtkPolyDataMapper()
headMapper.SetInputConnection(head.GetOutputPort())

headActor = vtk.vtkActor()
headActor.SetMapper(headMapper)

# Body
body = vtk.vtkSphereSource()
body.SetCenter(20, 0, 0)
body.SetRadius(10.0)
body.SetThetaResolution(50)

bodyMapper = vtk.vtkPolyDataMapper()
bodyMapper.SetInputConnection(body.GetOutputPort())

bodyActor = vtk.vtkActor()
bodyActor.SetMapper(bodyMapper)

# Nose
nose = vtk.vtkConeSource()
nose.SetCenter(40, 0, 0)
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
renderer.AddActor(headActor)
renderer.AddActor(bodyActor)
renderer.AddActor(noseActor)

# Color picked from the demo video
renderer.SetBackground(1, 0.894, 0.898)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(renderer)
renWin.SetSize(600, 600)

for i in range(0, 360):
    time.sleep(0.03)

    renWin.Render()
    renderer.GetActiveCamera().Azimuth(1)
