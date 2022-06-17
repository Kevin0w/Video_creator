# Loading all the packages required
import os
import eyed3
from PIL import Image
from pathlib import Path
from moviepy import editor
from mutagen.mp3 import MP3

'''
Creating class MP3ToMP4 which contains methods to convert
an audio to a video using a list of images.
'''


class MP3ToMP4:

    def __init__(self, folder_path, audio_path, video_path_name):
        """
        :param folder_path: contains the path of the root folder.
        :param audio_path: contains the path of the audio (mp3 file).
        :param video_path_name: contains the path where the created
                                video will be saved along with the
                                name of the created video.
        """
        self.folder_path = folder_path
        self.audio_path = audio_path
        self.video_path_name = video_path_name

        # Calling the create_video() method.
        self.create_video()

    def get_length(self):
        """
        This method reads an MP3 file and calculates its length
        in seconds.

        :return: length of the MP3 file
        """
        song = MP3(self.audio_path)
        # print(song.info.length)
        return int(song.info.length)

    def get_images(self):
        """
        This method reads the filenames of the images present
        in the folder_path of type '.png' and stores it in the
        'images' list.

        Then it opens the images, resizes them and appends them
        to another list, 'image_list'

        :return: list of opened images
        """
        path_images = Path(self.folder_path)
        images = list(path_images.glob('*.jpg'))
        image_list = list()
        for image_name in images:
            image = Image.open(image_name).resize((1920, 1080), Image.ANTIALIAS)
            image_list.append(image)
        return image_list

    def create_video(self):
        """
        This method calls the get_length() and get_images()
        methods internally. It then calculates the duration
        of each frame. After that, it saves all the opened images
        as a gif using the save() method. Finally it calls the
        combine_method()

        :return: None
        """
        length_audio = self.get_length()
        # length_audio = 693
        image_list = self.get_images()
        duration = int(length_audio / len(image_list)) * 10
        print(duration)
        image_list[0].save(self.folder_path + "temp.gif",
                           save_all=True,
                           append_images=image_list[1:],
                           duration=duration)

        # Calling the combine_audio() method.
        self.combine_audio()

    def combine_audio(self):
        """
        This method attaches the audio to the gif file created.
        It opens the gif file and mp3 file and then uses
        set_audio() method to attach the audio. Finally, it
        saves the video to the specified video_path_name

        :return: None
        """
        video = editor.VideoFileClip(self.folder_path + "temp.gif")
        audio = editor.AudioFileClip(self.audio_path)
        final_video = video.set_audio(audio)
        final_video.write_videofile(self.video_path_name, fps=60)


def concatenate_audio_moviepy(audio_clip_folder):
    """Concatenates several audio files into one audio file using MoviePy
    and save it to `output_path`. Note that extension (mp3, etc.) must be added to `output_path`"""
    audio_clip_paths = []

    for root, dirs, files in os.walk(audio_clip_folder, topdown=False):
        for file_name in files:
            if str(os.path.join(root, file_name)).endswith('mp3') or str(os.path.join(root, file_name)).endswith('m4a'):
                audio_clip_paths.append(os.path.join(root, file_name))

    clips = [editor.AudioFileClip(c) for c in audio_clip_paths]
    final_audio = editor.concatenate_audioclips(clips)
    final_audio.write_audiofile('music_video.mp3')
    final_audio.close()


def add_video_description(audio_clip_folder):
    general_descriptiohn = 'Best Gaming Music ♫♫ | Best EDM Mixes | NCS Releases | 2022 and more'

    with open('video_description.txt', 'w') as description_file:
        for root, dirs, files in os.walk(audio_clip_folder, topdown=False):
            for file_name in files:
                if str(os.path.join(root, file_name)).endswith('mp3') or str(os.path.join(root, file_name)).endswith(
                        'm4a'):
                    print(f"{str(os.path.join(root, file_name))}")
                    # song = MP3(str(os.path.join(root, file_name)))
                    song = MP3(r"E:\Github\Video_creator\music_video.mp3")
                    print(int(song.info.length) / 60)

                    # audio = eyed3.load(os.path.join(root, file_name))
                    # print("Title:", audio.tag.)
                    # print("Artist:", audio.tag.artist)
                    # print("Album:", audio.tag.album)
                    # print("Album artist:", audio.tag.album_artist)
                    # print("Composer:", audio.tag.composer)
                    # print("Publisher:", audio.tag.publisher)
                    # print("Genre:", audio.tag.genre.name)


def description():
    import mutagen
    from mutagen.wave import WAVE
    from mutagen.m4a import M4A

    # function to convert the information into
    # some readable format
    def audio_duration(length):
        hours = length // 3600  # calculate in hours
        length %= 3600
        mins = length // 60  # calculate in minutes
        length %= 60
        seconds = length  # calculate in seconds

        return hours, mins, seconds  # returns the duration

    # Create a WAVE object
    # Specify the directory address of your wavpack file
    # "alarm.wav" is the name of the audiofile
    audio = M4A(r"E:\Github\Video_creator\music_videos\5\music\Alva Gracia - Emotions Like [NCS Release].m4a")

    # contains all the metadata about the wavpack file
    audio_info = audio.info
    length = int(audio_info.length)
    hours, mins, seconds = audio_duration(length)
    print('Total Duration: {}:{}:{}'.format(hours, mins, seconds))


if __name__ == '__main__':
    # Taking the input for the paths of the variables mentioned below.
    # folder_path = input("Enter the Path of the Folder containing Images: ")
    # audio_path = input("Enter the Path of the MP3 file: ")
    # video_path_name = input("Enter the Path followed by name of the Video to be created: ")

    music_folder = r"E:\MusicHub\Videos\3\music"
    audio_path = 'music_video.mp3'
    folder_path = r"E:\MusicHub\Videos\3\thumbnail"
    video_path_name = r'E:\MusicHub\Videos\3\MUSIC_CHILL_EDM_NCS_BEST_GAMING.mp4'

    # Concatenating audio files into one
    concatenate_audio_moviepy(music_folder)

    # add_video_description(music_folder)
    # description()
    # Invoking the parameterized constructor of the MP3ToMP4 class.
    MP3ToMP4(folder_path, audio_path, video_path_name)
