# for each image in the specified directory, generate a relative path to the image and then save them all in a txt file

import os

path_prefix = "./medvision_dataset/images"
dir_names = ["train", "test", "val"]

if __name__ == "__main__":

    for dir_name in dir_names:
        dir_path = os.path.join(path_prefix, dir_name)
        if not os.path.exists(dir_path):
            print(f"Directory {dir_path} does not exist.")
            continue
        
        # Get all image files in the directory
        image_files = [f for f in os.listdir(dir_path) if f.endswith(('.jpg'))]
        
        # Generate relative paths and save to a text file
        with open(os.path.join(path_prefix, f"{dir_name}_medvision.txt"), 'w') as file:
            for image_file in image_files:
                relative_path = os.path.join("./images",dir_name, image_file)
                file.write(relative_path + '\n')
        
        print(f"Saved {len(image_files)} image paths to {dir_name}_image_paths.txt")