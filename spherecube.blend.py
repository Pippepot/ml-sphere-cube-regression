import bpy as bpy
import numpy as np

import blendtorch.btb as btb


def main():
    # parse script arguments passed via blendtorch launcher
    btargs, remainder = btb.parse_blendtorch_args()

    cam = bpy.context.scene.camera
    cube = bpy.data.objects["Cube"]
    original_mesh = cube.data.copy()
    random = [0]

    def pre_frame():
        cube.rotation_euler = np.random.uniform(0, np.pi, size=3)
        cube.select_set(True)
        cube.data = original_mesh.copy()
        cube.data.update()
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_all(action="SELECT")
        random[0] = np.random.rand()
        # interpolate cube to sphere
        bpy.ops.transform.tosphere(value=random[0])
        bpy.ops.object.mode_set(mode="OBJECT")

    def post_frame(off, pub):
        # publish image and sphere interpolation
        pub.publish(image=off.render(), value=random[0])

    pub = btb.DataPublisher(btargs.btsockets["DATA"], btargs.btid)
    cam = btb.Camera(shape=(240, 240))
    off = btb.OffScreenRenderer(camera=cam, mode="rgb")
    off.set_render_style(shading="RENDERED", overlays=False)

    # setup the animation and run endlessly
    anim = btb.AnimationController()
    anim.pre_frame.add(pre_frame)
    anim.post_frame.add(post_frame, off, pub)
    anim.play(frame_range=(0, 100), num_episodes=-1)


main()
