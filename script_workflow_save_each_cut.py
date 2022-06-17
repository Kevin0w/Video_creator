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

import time


def get_highlights_timestamp_list():
    cuts = [('00:20:54.000', '00:20:56.000'),
            ('00:21:54.000', '00:21:56.000')
            ]
    return cuts


def cut_video():
    import moviepy.editor as mpy
    start_time = time.time()
    vcodec = "libx264"
    videoquality = "24"
    IMAGEMAGICK_BINARY = "C:\\Program Files\\ImageMagick-7.1.0-Q16-HDRI\\magick.exe"
    # slow, ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
    compression = "medium"

    # Needed Input
    title = "first"
    loadtitle = r'E:\Projekt\2022-06-16 23-47-15.mp4'
    # audio_file = 'uncut_videos\\100T vs Soniqs _ VCT 2 NA Challengers 2 OPEN QUALIFIER 2022.webm'
    # savetitle = f'E:\\Projekt\\cut_{n}.mp4'

    # Opening the input
    video = mpy.VideoFileClip(loadtitle)
    # audio_clip = mpy.AudioFileClip(audio_file)

    cuts = get_highlights_timestamp_list()

    # cut file
    clips = []
    audios = []
    n = 1
    for cut in cuts:
        clip = video.subclip(cut[0], cut[1])
        # audio = audio_clip.subclip(cut[0], cut[1])
        clips.append(clip)
        final_clip = mpy.CompositeVideoClip(clips)
        final_clip.write_videofile(f'E:\\Projekt\\cut_{n}.mp4', threads=5, fps=60,
                                   codec=vcodec,
                                   preset=compression,
                                   ffmpeg_params=["-crf", videoquality])
        clips.pop(0)
        n += 1
        # audios.append(audio)

    # final_clip = mpy.concatenate_videoclips(clips)
    # final_audio = mpy.concatenate_audioclips(audios)

    # final_clip = mpy.CompositeVideoClip([video])
    # final_clip = final_clip.set_audio(final_audio)

    # save file
    # final_clip.write_videofile(savetitle, threads=5, fps=60,
    #                            codec=vcodec,
    #                            preset=compression,
    #                           ffmpeg_params=["-crf", videoquality])

    video.close()
    print(f"Duration: {int((time.time() - start_time) / 60)} minutes")


def main():
    cut_video()


if __name__ == '__main__':
    main()
