from pytubefix import YouTube

print("Welcome to ManiYTD - CLI Youtube Downloader!\n\n1. Download Video\n2. Download Audio\n")

choice = input("Enter Choice: ")

while choice not in ['1','2']:
    print("Please enter a valid choice!\n")
    choice = input("Enter Choice: ")

url = input("Enter the URL: ")

err = 0

try:
    yt = YouTube(url)
    title = yt.title
    print("\nDownloading - " + title)
    if choice==1:
         yt.streams.order_by("resolution").desc().first().download(output_path="Output/Video")

    elif choice==2:
        yt.streams.get_audio_only().download(output_path="Output/Audio")

except:
    print("\nError Occured!")
    err = 1


finally:

    print("Download successful!") if err == 0 else print("Download failed!")

