"""A video player class."""

from .video_library import VideoLibrary
from .video import Video
import random
from .video_playlist import Playlist


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.video_now = None  # video playing now
        self.video_paused = False  # video is not paused
        self.playlists = dict()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        videos = self._video_library.get_all_videos()
        videos.sort(key=lambda x: x.title)
        print("Here's a list of all available videos:")
        for video in videos:
            print(f"  {video.title} ({video.video_id}) [{' '.join(video.tags)}]")

    def play_video(self, video_id):

        if self._video_library.get_video(video_id) is None:
            print("Cannot play video: Video does not exist")

        elif self.video_now is not None:
            print(f"Stopping video: {self.video_now.title}")
            print(f"Playing video: {self._video_library.get_video(video_id).title}")
            self.video_now = self._video_library.get_video(video_id)
            self.video_paused = False

        else:
            print(f"Playing video: {self._video_library.get_video(video_id).title}")
            self.video_now = self._video_library.get_video(video_id)

    def stop_video(self):
        if self.video_now is not None:
            print(f"Stopping video: {self.video_now.title}")
            self.video_now = None

        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        videos = self._video_library.get_all_videos()

        if self.video_now is not None:
            print(f"Stopping video: {self.video_now.title}")
            video_random = random.choice(videos)
            self.video_now = video_random
            print(f"Playing video: {video_random.title}")
        else:
            video_random = random.choice(videos)
            self.video_now = video_random
            print(f"Playing video: {video_random.title}")

    def pause_video(self):
        if self.video_now is not None:
            if not self.video_paused:
                print(f"Pausing video: {self.video_now.title}")
                self.video_paused = True
            else:
                print(f"Video already paused: {self.video_now.title}")
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        if self.video_now is not None:
            if not self.video_paused:
                print(f"Cannot continue video: Video is not paused")
            else:
                print(f"Continuing video: {self.video_now.title}")
        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        if self.video_now is not None:
            if not self.video_paused:
                print(
                    f"Currently playing: {self.video_now.title} ({self.video_now.video_id}) [{' '.join(self.video_now.tags)}]")
            else:
                print(
                    f"Currently playing: {self.video_now.title} ({self.video_now.video_id}) [{' '.join(self.video_now.tags)}] - PAUSED")

        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        if self.playlists.__contains__(playlist_name.lower()):
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self.playlists[playlist_name.lower()] = Playlist(playlist_name)
            print(f"Successfully created new playlist: {playlist_name}")

    def add_to_playlist(self, playlist_name, video_id):
        if self.playlists.__contains__(playlist_name.lower()):
            if self._video_library.get_video(video_id) is None:
                print(f"Cannot add video to {playlist_name}: Video does not exist")
            else:
                if self.playlists[playlist_name.lower()].__contains__(video_id):
                    print(f"Cannot add video to {playlist_name}: Video already added")
                else:
                    self.playlists[playlist_name.lower()].__add__(video_id)
                    print(f"Added video to {playlist_name}: {self._video_library.get_video(video_id).title}")
        else:
            print("Cannot add video to another_playlist: Playlist does not exist")

    def show_all_playlists(self):
        if len(self.playlists) == 0:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            playlists = list(self.playlists.values())
            playlists.sort(key=lambda x: x.name)
            for playlist in playlists:
                print(f"  {playlist.name}")

    def show_playlist(self, playlist_name):
        if self.playlists.__contains__(playlist_name.lower()):
            print(f"Showing playlist: {playlist_name}")
            if len(self.playlists[playlist_name.lower()]) == 0:
                print("  No videos here yet")
            else:
                for x in self.playlists[playlist_name.lower()].videos:
                    video = self._video_library.get_video(x)
                    print(f"  {video.title} ({video.video_id}) [{' '.join(video.tags)}]")
        else:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")

    def remove_from_playlist(self, playlist_name, video_id):
        if self.playlists.__contains__(playlist_name.lower()):
            if self._video_library.get_video(video_id) is None:
                print(f"Cannot remove video from {playlist_name}: Video does not exist")
            else:
                if self.playlists[playlist_name.lower()].__contains__(video_id):
                    self.playlists[playlist_name.lower()].remove(video_id)
                    print(f"Removed video from {playlist_name}: {self._video_library.get_video(video_id).title}")
                else:
                    print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
        else:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")

    def clear_playlist(self, playlist_name):
        if self.playlists.__contains__(playlist_name.lower()):
            self.playlists[playlist_name.lower()].clear()
            print(f"Successfully removed all videos from {playlist_name}")
        else:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")

    def delete_playlist(self, playlist_name):
        if self.playlists.__contains__(playlist_name.lower()):
            self.playlists.pop(playlist_name.lower())
            print(f"Deleted playlist: {playlist_name}")
        else:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")


    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")