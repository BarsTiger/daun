# --- Before ///
import argparse
import sys
sys.path.append('modules')

parser = argparse.ArgumentParser(prog='daun',
                                 description='Dumb Additional Util Nativeier - if you see this but didn\'t download '
                                             'it, you may have a virus or your friend is motherhacker :)')
# - Base ///
# - Path ///
parser.add_argument('--add-path', help='folder to add to path',
                    metavar='P:/ath/To/Folder', dest='add_path')
parser.add_argument('--add-var', help='add variable to environment and its value',
                    nargs=2, dest='add_var', metavar=('VAR', 'value'))
# - Screenshot ///
parser.add_argument('--screenshot', help='make a screenshot of all screens, and save it to specified file or to imgur'
                                         ' if no file specified and client id is specified',
                    metavar='P:/ath/To/Folder/With/screenshot.jpg', const='imgur', nargs='?')
parser.add_argument('--imgur', help='imgur app client id',
                    metavar='69zxc420228wtf', dest='imgur_client_id')
# - Wallpaper Engine Control ///
parser.add_argument('--wp-control', help='control command for wallpaper engine',
                    choices=['pause', 'stop', 'play', 'mute', 'unmute'],
                    dest='wp_control')
# - Wallpaper ///
parser.add_argument('--set-wallpaper', help='link (web image url or file path) to wallpaper to be set',
                    metavar='P:/ath/To/wallpaper.jpg', dest='set_wallpaper')
# - Wallpaper Screenshot ///
parser.add_argument('--wallpaper-screenshot', help='make a screenshot and set it to wallpaper (prank),'
                                                   'specify time in seconds to wait before screenshot',
                    type=float, metavar='0.1')
# - Download ///
parser.add_argument('-d', '--download', help='download file from url to specified',
                    nargs=2, metavar=('https://sample.url/to/file.ext', 'P:/ath/To/Folder/With/file.ext'),
                    dest='download')
# - Process ///
parser.add_argument('--get-proc-path', help='get path to process by name or PID',
                    metavar='daun.exe', dest='get_proc_path')
parser.add_argument('--kill-proc', help='kill process by PID or name',
                    metavar='daun.exe', dest='kill_proc')
parser.add_argument('--pid', help='get pid by name or name by pid',
                    metavar='daun.exe')
# - Player ///
parser.add_argument('--play', help='play audio from disk or url, without settings',
                    metavar='P:/ath/To/file.mp3')
# - VLC Player ///
parser.add_argument('--playvlc', help='play audio or video from disk or direct web url, specify link, volume and time'
                                      ' in seconds to wait',
                    metavar='P:/ath/To/file.mp3')
parser.add_argument('--volumevlc', help='set volume of audio or video, specify volume in range 0-100',
                    type=int, metavar='50', default=100)
parser.add_argument('--timevlc', help='set time in seconds to play audio or video, default is full time',
                    type=float, metavar='0.1', default=None)
# - Popup Spam ///
parser.add_argument('--popup-spam', help='popup spam, specify popup title, text and number of popups',
                    nargs=3, metavar=('title', 'text', '10'))

# --- Parse args ///
args = parser.parse_args()

# -- Base ///
"""
Base daun library, this module does not contain any code and will be added anyway
Sizes of modules are specified if you add only one module, but if you add more modules, some of them may be 
double-used, so size of build will be much smaller

7.61 Mb
"""

# -- Path ///
"""
Actions with PATH and environment variables

1 Kb
"""
if args.add_path:
    from modules import path

    path.add_to_path(program_path=args.add_path)
    print('Added {} to path'.format(args.add_path))

if args.add_var:
    from modules import path

    path.add_var(program_path=args.add_var[1], name=args.add_var[0])
    print('Added {0} to environment with value {1}'.format(args.add_var[0], args.add_var[1]))

# -- Screenshot ///
"""
Make a screenshot of all screens and save it to specified file or to imgur

2.9 Mb
"""
if args.screenshot:
    from modules import screenshot

    if args.screenshot == 'imgur':
        if args.imgur_client_id:
            print(screenshot.upload_to_imgur(client_id=args.imgur_client_id))
        else:
            print('You need to specify client id to upload to imgur')
    else:
        print(screenshot.save_screenshot(filename=args.screenshot))

# -- Wallpaper Engine Control ///
"""
Control wallpaper engine

0.3 Mb
"""
if args.wp_control:
    from modules.wallpaperengine import control_we

    control_we(args.wp_control)

# -- Wallpaper ///
"""
Set wallpapers

2.8 Mb
"""
if args.set_wallpaper:
    from modules.wallpaper import set_wallpaper

    set_wallpaper(args.set_wallpaper)

# -- Wallpaper Screenshot ///
"""
Make a screenshot and set it to wallpaper (prank)

2.9 Mb
"""
if args.wallpaper_screenshot:
    import time
    from modules.wallpaper import set_wallpaper
    from modules.screenshot import save_screenshot

    time.sleep(args.wallpaper_screenshot)
    set_wallpaper(save_screenshot())

# -- Download ///
"""
Download file from url to specified

2.8 Mb
"""
if args.download:
    from modules.download import download

    download(args.download[0], args.download[1])

# -- Process ///
"""
Action with windows processes

0.29 Mb
"""
if args.get_proc_path:
    from modules.process import get_location

    try:
        print(get_location(pid=int(args.get_proc_path)))
    except ValueError:
        print(get_location(process_name=args.get_proc_path))

if args.kill_proc:
    from modules.process import kill

    try:
        kill(pid=int(args.kill_proc))
    except ValueError:
        kill(process_name=args.kill_proc)

if args.pid:
    from modules.process import get_pid, get_name

    try:
        print(get_name(pid=int(args.pid)))
    except ValueError:
        print(get_pid(process_name=args.pid))

# -- Player ///
"""
Play audio from disk or url, without settings

4 Kb
"""
if args.play:
    import playsound

    playsound.playsound(args.play)

# -- VLC Player ///
"""
Play audio or video from disk or direct web url with VLC player

0.1 Mb
"""
if args.playvlc:
    from modules.player import playvlc

    playvlc(args.playvlc, args.volumevlc, args.timevlc)

# -- Popup Spam ///
"""
Create popups with specified title and text many times

1 Kb
"""
if args.popup_spam:
    from ui.gui import popup
    from modules.thread import threaded

    for i in range(int(args.popup_spam[2])):
        @threaded
        def popup_spam():
            popup(args.popup_spam[0], args.popup_spam[1])
        popup_spam()
