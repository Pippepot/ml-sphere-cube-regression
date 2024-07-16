from pathlib import Path
from torch.utils import data
from PIL import Image
import blendtorch.btt as btt


def main():
    launch_args = dict(
        scene=Path(__file__).parent / "spherecube.blend",
        script=Path(__file__).parent / "spherecube.blend.py",
        num_instances=4,
        named_sockets=["DATA"],
    )

    # launch Blender
    with btt.BlenderLauncher(**launch_args) as bl:
        addr = bl.launch_info.addresses["DATA"]
        ds = btt.RemoteIterableDataset(addr, max_items=520)
        dl = data.DataLoader(ds, batch_size=16, num_workers=4)

        dataset = ""
        step = 0
        for item in dl:
            # item is a dict with image and sphere interpolation (value) (defined in spherecube.blend.py)
            img, value = item["image"], item["value"]
            print("Received", img.shape, value)
            for b in range(img.shape[0]):
                image = Image.fromarray(img[b].numpy())
                name = f"output_{step}.png"
                image.save(f"./data/{name}")
                step += 1
                dataset += name + "\n"
                dataset += str(value[b].numpy()) + "\n"

        with open("./data/dataset.txt", "w") as f:
            f.write(dataset)


if __name__ == "__main__":
    main()
