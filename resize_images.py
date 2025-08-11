from PIL import Image
import os

# Resize image function
def resize_image(image_path, save_path, new_width=800):
    with Image.open(image_path) as img:
        original_size = img.size  # Get original image size (width, height)
        
        # Calculate the new height maintaining aspect ratio
        width_percent = new_width / float(img.size[0])
        new_height = int(float(img.size[1]) * float(width_percent))
        
        # Resize the image using LANCZOS (equivalent to ANTIALIAS)
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Save the resized image
        img.save(save_path)
        
        print(f"Original Size: {original_size}, Resized Size: {(new_width, new_height)}")

# Function to process all images in a folder
def resize_images_in_folder(input_folder, output_folder, new_width=800):
    if not os.path.exists(output_folder):  # Check if the output folder exists
        os.makedirs(output_folder)  # If not, create the folder

    # Loop through all files in the folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith(('jpg', 'jpeg', 'png')):  # Check if file is an image
            image_path = os.path.join(input_folder, file_name)  # Get the full file path
            save_path = os.path.join(output_folder, f"resized_{file_name}")  # Define where to save the resized image
            resize_image(image_path, save_path, new_width)  # Resize the image

# Define input and output folders
input_folder = 'D:/Rohith files/Internship tasks/Task 7/Images_to_resize'  # Path to your images folder
output_folder = 'D:/Rohith files/Internship tasks/Task 7/Resized_images'

# Call the function to resize images
resize_images_in_folder(input_folder, output_folder)
