"""
folder with sounds/songs: 10 for example
folder with wallpaper for the video: 1

Expected result:
    10 - 30 minute video with wallpaper






# modify these start and end times for your subclips
cuts = [('00:00:02.949', '00:00:04.152'),
        ('00:00:06.328', '00:00:13.077')]

cuts = [('00:00:00.949', '00:00:00.152'),
        ('00:00:06.328', '00:00:13.077')]


def edit_video(loadtitle, savetitle, cuts):
    # load file
    video = mpy.VideoFileClip(loadtitle)

    # cut file
    clips = []
    for cut in cuts:
        clip = video.subclip(cut[0], cut[1])
        clips.append(clip)

    final_clip = mpy.concatenate_videoclips(clips)

    # add text
    # txt = mpy.TextClip('Please Subscribe!', font='Courier',
    #                   fontsize=120, color='white', bg_color='gray35')
    # txt = txt.set_position(('center', 0.6), relative=True)
    # txt = txt.set_start((0, 3))  # (min, s)
    # txt = txt.set_duration(4)
    # txt = txt.crossfadein(0.5)
    # txt = txt.crossfadeout(0.5)

    final_clip = mpy.CompositeVideoClip([video])

    # save file
    final_clip.write_videofile(savetitle, threads=4, fps=24,
                               codec=vcodec,
                               preset=compression,
                               ffmpeg_params=["-crf", videoquality])

    video.close()
"""

import os
import time
import moviepy.editor as mpy

start_time = time.time()
vcodec = "libx264"
videoquality = "24"
IMAGEMAGICK_BINARY = "C:\\Program Files\\ImageMagick-7.1.0-Q16-HDRI\\magick.exe"
# slow, ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
compression = "medium"

audio_clip_paths = []


def get_highlights_timestamp_list():
    cuts = [('00:01:10.000', '00:01:44.000'),
            ('00:03:00.000', '00:03:48.000'),
            ('00:04:31.000', '00:05:13.000'),
            ('00:06:49.000', '00:07:25.000'),
            ('00:08:20.000', '00:09:08.000'),
            ('00:10:14.000', '00:11:05.000'),
            ('00:11:46.000', '00:12:51.000'),
            ('00:14:28.000', '00:15:18.000'),
            ('00:16:20.000', '00:16:48.000'),
            ('00:18:43.000', '00:19:20.000'),
            ('00:20:16.000', '00:21:19.000'),
            ('00:22:15.000', '00:23:00.000'),
            ('00:23:20.000', '00:23:58.000'),
            ('00:24:46.000', '00:25:33.000'),
            ('00:26:13.000', '00:27:08.000'),
            ('00:28:31.000', '00:29:19.000'),
            ('00:30:08.000', '00:30:49.000'),
            ('00:31:38.000', '00:32:30.000'),
            ('00:33:08.000', '00:33:55.000'),
            ('00:34:50.000', '00:36:00.000'),
            ('00:36:34.000', '00:37:45.000'),
            ('00:39:24.000', '00:40:45.000'),
            ('00:41:20.000', '00:42:23.000'),
            ('00:43:08.000', '00:44:00.000'),
            ('00:44:50.000', '00:46:00.000'),
            ('00:46:37.000', '00:47:26.000'),
            ('00:48:04.000', '00:48:46.000'),
            ('00:49:33.000', '00:50:50.000'),
            ('00:51:20.000', '00:52:10.000'),
            ('00:52:41.000', '00:53:19.000'),
            ('00:54:04.000', '00:55:13.000'),
            ('00:55:49.000', '00:56:42.000'),
            ('00:57:31.000', '00:58:11.000')]
    return cuts


def cut_video():
    # Needed Input
    title = "first"
    loadtitle = 'uncut_videos\\100T vs Soniqs _ VCT 2 NA Challengers 2 OPEN QUALIFIER 2022.mp4'
    audio_file = 'uncut_videos\\100T vs Soniqs _ VCT 2 NA Challengers 2 OPEN QUALIFIER 2022.webm'
    savetitle = 'YT_ready_videos\\YT_ready.mp4'

    # Opening the input
    video = mpy.VideoFileClip(loadtitle)
    audio_clip = mpy.AudioFileClip(audio_file)

    cuts = get_highlights_timestamp_list()

    # cut file
    clips = []
    audios = []
    for cut in cuts:
        clip = video.subclip(cut[0], cut[1])
        audio = audio_clip.subclip(cut[0], cut[1])
        clips.append(clip)
        audios.append(audio)

    final_clip = mpy.concatenate_videoclips(clips)
    final_audio = mpy.concatenate_audioclips(audios)

    # final_clip = mpy.CompositeVideoClip([video])
    final_clip = final_clip.set_audio(final_audio)

    # save file
    final_clip.write_videofile(savetitle, threads=5, fps=60,
                               codec=vcodec,
                               preset=compression,
                               ffmpeg_params=["-crf", videoquality])

    video.close()
    print(f"Duration: {int((time.time() - start_time) / 60)} minutes")


def concatenate_audio_moviepy(audio_clip_folder):
    """Concatenates several audio files into one audio file using MoviePy
    and save it to `output_path`. Note that extension (mp3, etc.) must be added to `output_path`"""

    for root, dirs, files in os.walk(audio_clip_folder, topdown=False):
        for file_name in files:
            if str(os.path.join(root, file_name)).endswith('mp3'):
                audio_clip_paths.append(os.path.join(root, file_name))

    clips = [mpy.AudioFileClip(c) for c in audio_clip_paths]
    final_audio = mpy.concatenate_audioclips(clips)
    final_audio.write_audiofile('music_video.mp3')


def create_music_video(music_folder, wallpaper):
    # concatenate_audio_moviepy(music_folder)

    files = [wallpaper]
    # for i in range(24):
    #    files.append(wallpaper)

    final_music_video = mpy.ImageSequenceClip(files, durations=[10])
    final_music_video.set_audio('music_video.mp3')

    final_music_video.write_videofile("music_video.mp4",
                                      ffmpeg_params=["-crf", videoquality],
                                      fps=24,
                                      audio_codec='libvorbis',
                                      preset=compression,
                                      threads=5)

    final_music_video.close()

    print(f"Duration: {int((time.time() - start_time) / 60)} minutes")


def main():
    # cut_video()
    music_folder = r"E:\Github\Video_creator\music"
    wallapaper = r"E:\Github\Video_creator\wallpapers\anime-girl-headphones-looking-away-4k-ls.jpg"

    # https://hdqwalls.com/anime-girl-headphones-looking-away-4k-wallpaper
    create_music_video(music_folder, wallapaper)


if __name__ == '__main__':
    main()
