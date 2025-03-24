import yaml
from custom_modules.io import load_image, show_image
from custom_modules.process import luminance
from cymods.primes import primes

def main():
    # with open("config.yml", "r") as f:
    #     config = yaml.safe_load(f)
 
    # img = load_image(config["test_img_path"])
    # processed_img = luminance(img)
    # show_image(processed_img)

    # test primes 
    print(primes(1000))


if __name__ == "__main__":
    main()
