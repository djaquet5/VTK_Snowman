"""
Lab: 1-Snowman
Authors: David Jaquet, Luc Wachter
Description: Reproduce the video at the following link using VTK and its python wrapper
             https://youtu.be/hthbXe_boXc
Python version: 3.7.4
"""

import vtk
import time

FRAME_TIME = 0.01


# Generate an actor with a sphere shape
def get_sphere_actor(pos, radius):
    """Returns a sphere actor at the position and of the size specified"""
    sphere = vtk.vtkSphereSource()
    sphere.SetCenter(pos)
    sphere.SetRadius(radius)
    sphere.SetPhiResolution(50)
    sphere.SetThetaResolution(50)  # TODO: Different resolutions for different sizes

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(sphere.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    return actor


def get_cone_actor(center_position, height, radius):
    """Returns a cone actor at the position and of the size specified"""
    cone = vtk.vtkConeSource()
    cone.SetDirection(0, -90, 0)
    cone.SetCenter(center_position)
    cone.SetHeight(height)
    cone.SetRadius(radius)
    cone.SetResolution(50)

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(cone.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    return actor


def display_loop(range_end, display_func, value):
    """Executes a given display action for the given amount of frames"""
    for _ in range(range_end):
        time.sleep(FRAME_TIME)

        renWin.Render()
        display_func(value)


def change_actor_y(actor, delta):
    """Moves an actor up or down by delta"""
    position = actor.GetPosition()
    actor.SetPosition(position[0], position[1] + delta, position[2])


def raise_and_rotate_x(actor, delta_y, delta_rotate):
    """Moves an actor up or down by delta and rotates it on the pitch axis"""
    change_actor_y(actor, delta_y)
    actor.RotateX(delta_rotate)


# Main instructions
if __name__ == '__main__':
    head = get_sphere_actor([-20, 0, 0], radius=8)
    body = get_sphere_actor([0, 0, 0], radius=10)

    nose = get_cone_actor((28, 0, 0), height=3.0, radius=1.0)
    nose.GetProperty().SetColor(0.925, 0.65, 0)

    # Renderer
    renderer = vtk.vtkRenderer()
    renderer.AddActor(head)
    renderer.AddActor(body)
    renderer.AddActor(nose)

    # Color picked from the demo video
    renderer.SetBackground(1, 0.894, 0.898)

    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(renderer)
    renWin.SetSize(600, 600)

    # Align the head with the body
    display_loop(180, head.RotateZ, -0.5)

    # Lower the head onto the body
    display_loop(30, lambda x: change_actor_y(head, x), -0.1)

    # TODO: Align the nose with the body
    # FIXME: Edit range, the nose disapear in front of camera
    # display_loop(1000, noseActor.RotateY, -0.5)

    # TODO: The nose should be inside the head
    display_loop(180, lambda x: raise_and_rotate_x(nose, x, -0.4), 0.1)

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
