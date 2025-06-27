import cv2

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames

def save_video(output_video_frames, output_video_path):
    if not output_video_frames:
        print("Error: No frames to save.")
        return

    height, width = output_video_frames[0].shape[:2]

    # Use MP4V for .mp4 and XVID for .avi
    if output_video_path.endswith('.avi'):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
    elif output_video_path.endswith('.mp4'):
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    else:
        print("Unsupported video format. Use .avi or .mp4")
        return

    out = cv2.VideoWriter(output_video_path, fourcc, 24, (width, height))

    if not out.isOpened():
        print(f"Error: Failed to open VideoWriter with path: {output_video_path}")
        return

    for frame in output_video_frames:
        out.write(frame)

    out.release()
    print("Video saved.")
