import argparse

parser = argparse.ArgumentParser(prog='daun',
                                 description='Dumb Additional Util Nativeier - if you see this but didn\'t download '
                                             'it, you may have a virus or your friend is motherhacker :)')
parser.add_argument('--add-path', help='folder to add to path',
                    metavar='P:/ath/To/Folder', dest='add_path')
parser.add_argument('--add-var', help='add variable to environment and its value',
                    nargs=2, dest='add_var', metavar=('VAR', 'value'))
parser.add_argument('--screenshot', help='make a screenshot of all screens, and save it to specified file or to imgur'
                                         ' if no file specified and client id is specified',
                    metavar='P:/ath/To/Folder/With/screenshot.jpg', const='imgur', nargs='?')
parser.add_argument('--imgur', help='imgur app client id',
                    metavar='69zxc420228wtf', dest='imgur_client_id')
parser.add_argument('--wp-control', help='control command for wallpaper engine',
                    choices=['pause', 'stop', 'play', 'mute', 'unmute'],
                    dest='wp_control')
parser.add_argument('--set-wallpaper', help='link (web image url or file path) to wallpaper to be set',
                    metavar='P:/ath/To/wallpaper.jpg', dest='set_wallpaper')
parser.add_argument('-d', '--download', help='download file from url to specified',
                    nargs=2, metavar=('https://sample.url/to/file.ext', 'P:/ath/To/Folder/With/file.ext'),
                    dest='download')

args = parser.parse_args()


if args.add_path:
    from modules import path
    path.add_to_path(program_path=args.add_path)
    print('Added {} to path'.format(args.add_path))


if args.add_var:
    from modules import path
    path.add_var(program_path=args.add_var[1], name=args.add_var[0])
    print('Added {0} to environment with value {1}'.format(args.add_var[0], args.add_var[1]))


if args.screenshot:
    from modules import screenshot
    if args.screenshot == 'imgur':
        if args.imgur_client_id:
            print(screenshot.upload_to_imgur(client_id=args.imgur_client_id))
        else:
            print('You need to specify client id to upload to imgur')
    else:
        print(screenshot.save_screenshot(filename=args.screenshot))


if args.wp_control:
    from modules.wallpaperengine import control_we
    control_we(args.wp_control)


if args.set_wallpaper:
    from modules.wallpaper import set_wallpaper
    set_wallpaper(args.set_wallpaper)


if args.download:
    from modules.download import download
    download(args.download[0], args.download[1])
