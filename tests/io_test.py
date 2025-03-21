import yaml

def test_load_image():
    from python_modules.io import load_image

    with open("config.yml", "r") as f:
        config = yaml.safe_load(f)
    img = load_image(config["test_img_path"])
    assert img is not None
    assert img.shape == (512, 512, 3)
