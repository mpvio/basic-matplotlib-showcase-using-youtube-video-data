import matplotlib.pyplot as plt
import controller.video_controller as video_controller

# track views over time
video = video_controller.read_json_to_video()
(times, view_counts) = video_controller.get_N_axes(video, "view")
plt.plot(times, view_counts)
plt.xlabel("Time")
plt.ylabel("View Count")
plt.title(video.snippet.title)
plt.show()