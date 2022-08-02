# All imports are needed for the second task
import os
from TikTokApi import TikTokApi
from moviepy.editor import VideoFileClip


# Task #1
s = "Python Bootcamp"
h = hash(s)
print(h)
# saving the hash and the value into a hash table to have access to the data in future
hash_table = {h: s}
print(hash_table[hash(s)])


# Task #2

# The URL from the example is not available, so I chose another one that works
URL = 'https://www.tiktok.com/@patron__dsns/video/7110916951626599685?\
    is_copy_url=1&is_from_webapp=v1'

def convert_video_to_gif(url, fps=30):
    """This function gets id video from URL, creates file name by id, gets video by id
    and converts it to bytes, writes bytes in a file, converts the file to gif
    (depends on fps), deletes video file, and returns a path to the gif file
    """
    api = TikTokApi()
    output_folder = 'output'

    try:
        os.mkdir(output_folder)
    except FileExistsError:
        pass
    finally:
        output_folder = os.path.join(os.path.abspath(os.getcwd()), output_folder)

    vid_id = url.split('video/')[1].split('?')[0]
    vid_file_name, gif_file_name = f'{vid_id}.mp4', f'{vid_id}.gif'
    video = api.video(id=vid_id)
    video_bytes = video.bytes()

    with open(vid_file_name, 'wb') as file:
        file.write(video_bytes)

    video_clip = VideoFileClip(vid_file_name, audio=False)
    file_path = os.path.join(output_folder, gif_file_name)
    video_clip.write_gif(file_path, fps=fps)

    os.remove(vid_file_name)
    return os.path.realpath(file_path)

print(convert_video_to_gif(URL))
