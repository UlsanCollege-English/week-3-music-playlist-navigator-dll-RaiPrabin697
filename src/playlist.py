# src/playlist.py

class Node:
    def __init__(self, song):
        self.song = song
        self.prev = None
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_song(self, title):
        """Add a song at the end of the playlist."""
        new_node = Node(title)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def to_list(self):
        """Return all songs in order as a list."""
        songs = []
        node = self.head
        while node:
            songs.append(node.song)
            node = node.next
        return songs

    def play_first(self):
        """Start playing from the first song."""
        if not self.head:
            return None
        self.current = self.head
        return self.current.song

    def next(self):
        """Move to the next song; stay at tail if already last."""
        if not self.current:
            return None
        if self.current.next:
            self.current = self.current.next
        return self.current.song

    def prev(self):
        """Move to the previous song; stay at head if already first."""
        if not self.current:
            return None
        if self.current.prev:
            self.current = self.current.prev
        return self.current.song

    def insert_after_current(self, title):
        """Insert a new song right after the current one."""
        if not self.current:
            return False
        new_node = Node(title)
        nxt = self.current.next
        self.current.next = new_node
        new_node.prev = self.current
        new_node.next = nxt
        if nxt:
            nxt.prev = new_node
        else:
            self.tail = new_node
        return True

    def remove_current(self):
        """Remove the current song. Move current to next if possible, otherwise to prev."""
        if not self.current:
            return False

        prev_node = self.current.prev
        next_node = self.current.next

        if prev_node:
            prev_node.next = next_node
        else:
            self.head = next_node

        if next_node:
            next_node.prev = prev_node
        else:
            self.tail = prev_node

        # update current
        self.current = next_node if next_node else prev_node
        return True
