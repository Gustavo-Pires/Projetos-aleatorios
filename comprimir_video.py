from moviepy.editor import VideoFileClip

def compress_video(input_path, output_path):
    video = VideoFileClip(input_path)
    compressed_video = video.resize(height=480)  # Adjust the height as needed
    compressed_video.write_videofile(output_path, codec="libx264", audio_codec="aac")

input_path = "/Users/Gustavo/Desktop/Video apresentacao.mp4"
output_path = "/Users/Gustavo/Desktop/Compressed Video.mp4"

compress_video(input_path, output_path)