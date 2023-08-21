from moviepy.editor import VideoFileClip

video_file_path = "./whisper/video.mp4"
video = VideoFileClip(video_file_path)
audio_file_path = "./whisper/audio.mp3"
video.audio.write_audiofile(audio_file_path)
