import pyglet


viewport = pyglet.window.Window()


@viewport.event
def on_draw():
    viewport.clear()


def teardown():
    pass


@viewport.event
def on_window_close():
    teardown()


pyglet.app.run()
