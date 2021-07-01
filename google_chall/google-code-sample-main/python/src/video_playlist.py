class Playlist:
    def __init__(self, name):
        self.name = name
        self.videos = []

    def __contains__(self, video_id):
        return self.videos.__contains__(video_id)

    def __add__(self, video_id):
        self.videos.append(video_id)
        

    def __len__(self):
        return len(self.videos)

    def remove(self, video_id):
        self.videos.remove(video_id)

    def clear(self):
        self.videos.clear()