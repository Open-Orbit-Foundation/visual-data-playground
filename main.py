import yaml
from python_modules.io import load_image, show_image
from python_modules.process import reversible_color_transform


def main():
    with open("config.yml", "r") as f:
        config = yaml.safe_load(f)
 
    img = load_image(config["test_img_path"])
    processed_img = reversible_color_transform(img)
    show_image(processed_img)

if __name__ == "__main__":
    main()
