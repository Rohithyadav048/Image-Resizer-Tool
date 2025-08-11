# Image Resizer Tool

A simple Python script that resizes images in a specified folder. This tool allows you to resize images while maintaining their aspect ratio. The resized images are saved in a new folder for easy access.

## Project Objective

The primary goal of this project is to create a tool that:
- Takes images from a specified folder.
- Resizes them to a fixed width (while maintaining their aspect ratio).
- Saves the resized images to a different folder.

This is useful for situations where you need to optimize images for web use or reduce image file sizes.

## Technologies Used

1. **Python 3** – Programming language
2. **Pillow (PIL)** – Python Imaging Library for image manipulation
3. **OS Library** – For interacting with the file system (folders and file handling)

## How It Works

1. The script first checks if the input folder (with images) exists.
2. The images in the folder are resized to a new width (default is 800px), and their aspect ratio is maintained.
3. The resized images are saved in the output folder with the prefix `resized_`.

### Example Usage:

1. **Set Input Folder**: Place the images you want to resize in the `Images_to_resize` folder.
2. **Set Output Folder**: The resized images will be saved in the `Resized_images` folder.
3. Run the script:

    ```bash
    python resize_images.py
    ```

### Example Output:

After running the script, the original and resized image dimensions are printed in the terminal like so:

Original Size: (680, 476), Resized Size: (800, 560)
Original Size: (680, 408), Resized Size: (800, 480)


## Project Structure

- **`resize_images.py`** – The Python script that resizes the images.
- **`Images_to_resize`** – The folder containing images to be resized (create this folder).
- **`Resized_images`** – The folder where resized images will be saved (this folder will be created by the script).
- **`README.md`** – Project documentation.

## How to Run

1. Clone or download this repository.
2. Place the images you want to resize in the `Images_to_resize` folder.
3. Run the following command to resize the images:

    ```bash
    python resize_images.py
    ```

4. Check the `Resized_images` folder for the resized images.

## Contribution

Feel free to fork this project and contribute by adding new features, fixing bugs, or improving the tool.
