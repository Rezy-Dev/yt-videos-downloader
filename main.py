import tkinter as tk
from pytube import YouTube

def download_video():
    url = url_input.get()
    
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download()
    
    url_input.delete(0, tk.END)
    
    message_label.config(text="Download complete!")

window = tk.Tk()
window.title("YouTube Video Downloader")

url_label = tk.Label(text="Enter YouTube URL:")
url_label.pack()

url_input = tk.Entry(width=50)
url_input.pack()

download_button = tk.Button(text="Download", command=download_video)
download_button.pack()

message_label = tk.Label(text="")
message_label.pack()

window.mainloop()
