import cv2
import os
import sys
import threading
from pydub import AudioSegment
from pydub.playback import play

def play_audio(audio_path):
    """Plays audio in a separate thread."""
    audio = AudioSegment.from_file(audio_path)
    play(audio)  # Blocks until audio finishes

def play_video(video_path):
    """Plays video in fullscreen without exit option."""
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}.")
        sys.exit(1)

    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_delay = int(1000 / fps) if fps > 0 else 30

    # Fullscreen window
    cv2.namedWindow("Video Player", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Video Player", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # Extract audio (runs in a separate thread)
    audio_thread = threading.Thread(target=play_audio, args=(video_path,))
    audio_thread.start()

    # Play video frames
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break  # Video ends

        cv2.imshow("Video Player", frame)
        cv2.waitKey(frame_delay)  # Frame timing

    cap.release()
    cv2.destroyAllWindows()
    audio_thread.join()  # Ensure audio finishes

if __name__ == "__main__":
    video_path = "video.mp4"
    if not os.path.exists(video_path):
        print(f"Error: {video_path} not found.")
        sys.exit(1)

    play_video(video_path)
