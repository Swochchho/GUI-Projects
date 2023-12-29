# Import necessary libraries
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
import traceback

# Function to download YouTube video
def download_video(url, save_path):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Filter and get the highest resolution progressive stream
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()

        # Download the video to the specified path
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully!")

    except Exception as e:
        # Handle exceptions during the download process
        print(f"Error downloading video: {e}")
        traceback.print_exc()

# Function to open a file dialog for selecting the download location
def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder

# Main function to run the script
def main():
    # Create a Tkinter root window and hide it
    root = tk.Tk()
    root.withdraw()

    try:
        # Get user input for the YouTube video URL
        video_url = input("Please input a YouTube video URL: ").strip()

        # Open file dialog to choose the download location
        save_dir = open_file_dialog()

        if save_dir:
            # If a valid download location is selected, initiate download
            print("Downloading...")
            download_video(video_url, save_dir)
        else:
            # If no valid download location is selected, print an error message
            print("Invalid save location!")

    except KeyboardInterrupt:
        # Handle keyboard interrupt (e.g., user cancels the download)
        print("Download canceled by user.")

    except Exception as e:
        # Handle unexpected errors during script execution
        print(f"Unexpected error: {e}")
        traceback.print_exc()

# Check if the script is the main program being run
if __name__ == "__main__":
    # Call the main function to start the script execution
    main()