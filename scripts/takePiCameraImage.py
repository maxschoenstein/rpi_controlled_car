import picamera
import time
import os

def take_pictures(output_dir, total_images, interval):
    with picamera.PiCamera() as camera:
        camera.resolution = (450, 200)  # Set the resolution of the camera
        camera.start_preview()           # Start a preview on the screen
        for i in range(total_images):
            # Capture the picture and save it to the specified file
            output_file = f"{output_dir}/image_{i+1}.jpg"
            camera.capture(output_file)
            print(f"Picture {i+1} taken and saved as {output_file}")
            if i < total_images - 1:
                print(f"Waiting {interval} seconds before taking next picture...")
                time.sleep(interval)   # Wait for the specified interval before capturing the next image
        camera.stop_preview()            # Stop the preview

if __name__ == "__main__":
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "rpi_camera")
    total_images = 1     
    interval = 0.5         

    os.makedirs(output_dir, exist_ok=True)

    take_pictures(output_dir, total_images, interval)
