import time


def playvlc(file_path, volume: int = 100, sleep: float = None):
    import vlc
    """
    Play a file with VLC
    """
    player = vlc.MediaPlayer(file_path)
    player.play()
    player.audio_set_volume(volume)
    time.sleep(0.5)
    if sleep is not None:
        time.sleep(sleep)
    else:
        time.sleep(player.get_length())
