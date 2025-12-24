import json
import time
from model.video import Video
def read_json_to_video() -> Video:
    with open("sample YT values.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        
    video = Video(
        id=data["id"],
        title=data["snippet"]["title"],
        description=data["snippet"]["description"],
        channel_title=data["snippet"]["channelTitle"],
        published_at=data["snippet"]["publishedAt"]
    )
    
    for stat in data["statistics"]:
        video.add_statistics(
            time= time.strptime(stat["time"], "%Y-%m-%dT%H:%M:%SZ"),
            view_count=stat["viewCount"],
            favorite_count=stat["favoriteCount"],
            comment_count=stat["commentCount"],
            like_count=stat["likeCount"],
            dislike_count=stat["dislikeCount"]
        )
        
    return video

def get_N_axes(video: Video, N: str) -> tuple[list, list]:
    times = [time.strftime("%Y-%m-%dT%H:%M:%SZ", stat.time) for stat in video.statistics]
    counts = []
    if N == "view":
        counts = [stat.view_count for stat in video.statistics]
    elif N == "like":
        counts = [stat.like_count for stat in video.statistics]
    elif N == "comment":
        counts = [stat.comment_count for stat in video.statistics]
    elif N == "favorite":
        counts = [stat.favorite_count for stat in video.statistics]
    elif N == "dislike":
        counts = [stat.dislike_count for stat in video.statistics]
    return times, counts