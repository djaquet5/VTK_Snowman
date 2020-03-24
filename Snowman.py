import vtk
import time


# Generate an actor with a sphere shape
def getSphereActor(posX, radius):
    sphere = vtk.vtkSphereSource()
    sphere.SetCenter(posX, 0, 0)
    sphere.SetRadius(radius)
    sphere.SetPhiResolution(40)
    sphere.SetThetaResolution(40)

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(sphere.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    return actor


head = getSphereActor(-20, 8)
body = getSphereActor(0, 10)

# Nose
nose = vtk.vtkConeSource()
nose.SetCenter(20, 0, 0)
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

for i in range(0, 360):
    time.sleep(0.03)

    renWin.Render()
    # renderer.GetActiveCamera().Azimuth(1)
    head.GetProperty().SetPosition(head.GetProperty().)
