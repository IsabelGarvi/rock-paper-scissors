class Bunch:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)


keys = Bunch(
    DOWN='\x1b[B',
    UP='\x1b[A',
    LEFT='\x1b[D',
    RIGHT='\x1b[C',
    ENTER='\x0a',  # ControlJ  (Identical to '\n')
    ESCAPE='\x1b',
    CONTROLC='\x03',
    BACK='\x7f')


def feed_app_with_input(type, message, text, **kwargs):
    """
    Create a CommandLineInterface, feed it with the given user input and return
    the CLI object.
    This returns a (result, CLI) tuple.
    note: this only works if you import your prompt and then this function!!
    """
    # If the given text doesn't end with a newline, the interface won't finish.
    assert text.endswith('\n')

    application = getattr(prompts, type).question(message, **kwargs)

    loop = PosixEventLoop()
    try:
        inp = PipeInput()
        inp.send_text(text)
        cli = CommandLineInterface(
            application=application,
            eventloop=loop,
            input=inp,
            output=DummyOutput())
        result = cli.run()
        return result, cli
    finally:
        loop.close()
        inp.close()
