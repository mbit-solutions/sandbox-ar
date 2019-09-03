import sys
import sandbox as sb
import config as cfg
import renderer as rd
import tkinter

fake_mode = False

if len(sys.argv) == 2 and sys.argv[1] == 'fakenect':
    fake_mode = True

if fake_mode == True:
    import fakenect as fa
    nect = fa.Fakenect()
else:
    import kinect as ki
    nect = ki.Kinect()

window = tkinter.Tk()
window.attributes('-fullscreen', True)
window.bind('<Escape>',lambda e: window.destroy())

config = cfg.Config()
sandbox = sb.Sandbox(config, nect, rd.Renderer(config))
sandbox.execute(window)