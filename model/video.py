from model.snippet import Snippet
from model.statistics import Statistics

class Video():
    statistics: list[Statistics] = []
    def __init__(self, id, title, description, channel_title, published_at):
        self.id = id
        self.snippet = Snippet(published_at, title, description, channel_title)
        
    def add_statistics(self, time, view_count, favorite_count, comment_count, like_count, dislike_count):
        stats = Statistics(time, view_count, favorite_count, comment_count, like_count, dislike_count)
        self.statistics.append(stats)