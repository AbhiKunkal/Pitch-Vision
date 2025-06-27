from utils import read_video, save_video
import cv2
import numpy as np
from trackers import Tracker

def main():
    # Read video
    video_frames = read_video('input_videos/08fd33_4.mp4')
    print(f"Total frames read: {len(video_frames)}")
    
    # Initialize tracker
    tracker = Tracker('models/best.pt')
    
    # Get tracks (don't read from stub for testing fresh)
    tracks = tracker.get_object_tracks(
        video_frames,
        read_from_stub=False,
        stub_path='stubs/track_stubs.pkl'
    )
    
    print(f"Tracks for players: {len(tracks['players'])}")
    
    # Draw annotations
    output_video_frames = tracker.draw_annotations(video_frames, tracks)
    print(f"Output frames after drawing: {len(output_video_frames)}")

    # Optional: Save some debug images to check drawing
    for i, frame in enumerate(output_video_frames[:5]):
        cv2.imwrite(f"debug_frame_{i}.png", frame)
    
    # Save video
    save_video(output_video_frames, 'output_videos/output_video.avi')
    print("Video saved.")

if __name__ == '__main__':
    main()
