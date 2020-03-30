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
def get_sphere_actor(pos, radius):
    """Returns a sphere source at the position and of the size specified"""
    sphere = vtk.vtkSphereSource()
    sphere.SetCenter(pos[0], pos[1], pos[2])
    sphere.SetRadius(radius)
    sphere.SetPhiResolution(50)
    sphere.SetThetaResolution(50)  # TODO: Different resolutions for different sizes

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(sphere.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    return actor


def display_loop(range_end, display_func, value):
    """Executes a given display action for the given amount of frames"""
    for i in range(0, range_end):
        time.sleep(0.03)

        renWin.Render()
        display_func(value)


def lower_actor(actor, delta):
    """Moves an actor down by delta"""
    position = actor.GetPosition()
    actor.SetPosition(position[0], position[1] - delta, position[2])


if __name__ == '__main__':
    head = get_sphere_actor([-20, 0, 0], 8)
    body = get_sphere_actor([0, 0, 0], 10)

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
    display_loop(180, head.RotateZ, -0.5)

    # Lower the head onto the body
    display_loop(30, lambda x: lower_actor(head, x), 0.1)

    # TODO: Align the nose with the body
    # FIXME: Edit range, the nose disapear in front of camera
    # display_loop(1000, noseActor.RotateY, -0.5)

    # TODO: The nose should be inside the head
    for i in range(0, 180):
        time.sleep(0.03)

        renWin.Render()

        position = noseActor.GetPosition()
        noseActor.SetPosition(position[0], position[1] + 0.1, position[2])
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
    leftEye = get_sphere_actor([-2, 18, 7], 1.5)
    leftEye.GetProperty().SetColor(0, 0, 0)

    rightEye = get_sphere_actor([2, 18, 7], 1.5)
    rightEye.GetProperty().SetColor(0, 0, 0)

    renderer.AddActor(leftEye)
    renderer.AddActor(rightEye)
    renWin.Render()

    # Roll the camera
    display_loop(360, renderer.GetActiveCamera().Roll, 1)

    # Traveling around the snowman
    display_loop(360, renderer.GetActiveCamera().Azimuth, 1)

    # Lift the camera to see the snowman from above
    display_loop(80, renderer.GetActiveCamera().Elevation, 1)

    # Lower the camera to have the snowman in front of the camera
    display_loop(80, renderer.GetActiveCamera().Elevation, -1)
