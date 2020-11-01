import enum
from ipywidgets import DOMWidget, CallbackDispatcher, widget_serialization, register
from traitlets import Unicode, Bool, Int, Instance, link

import pty, os, tty, termios, time, sys, base64, struct, signal
from fcntl import fcntl, F_GETFL, F_SETFL, ioctl
import threading
import time
# See js/lib/example.js for the frontend counterpart to this file.

@register
class IPyXterm(DOMWidget):
    # Name of the widget view class in front-end
    _view_name = Unicode('IPyXtermView').tag(sync=True)
    # Name of the widget model class in front-end
    _model_name = Unicode('IPyXtermModel').tag(sync=True)
    # Name of the front-end module containing widget view
    _view_module = Unicode('jupyter-xterm-widget').tag(sync=True)
    # Name of the front-end module containing widget model
    _model_module = Unicode('jupyter-xterm-widget').tag(sync=True)
    # Version of the front-end module containing widget view
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    # Version of the front-end module containing widget model
    _model_module_version = Unicode('^0.1.0').tag(sync=True)

    # Widget specific property.
    # Widget properties are defined as traitlets. Any property tagged with `sync=True`
    # is automatically synced to the frontend *any* time it changes in Python.
    # It is synced back to Python from the frontend *any* time the model is touched.

    # Display Properties

    # State Properties
    status = Bool(False).tag(sync=True)
    pid = Int(0).tag(sync=True)
    fd = Int(0).tag(sync=True)
    io_file = Instance('_io.FileIO', allow_none=True).tag(sync=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._submission_callbacks = CallbackDispatcher()
        self.on_msg(self._handle_string_msg)

        # Defining 
        self.status = False
        self.pid, self.fd = pty.fork()

        term_thread = threading.Thread(target=self.thread_tty)
        term_thread.start()

        while not self.io_file:
            print('Waiting for io_file')
            time.sleep(1)

        #if self.pid == pty.CHILD:
        #    os.execvp('bash', ['bash'])
        #else:
        #    term_thread = threading.Thread(target=self.thread_tty)
        #    term_thread.start()
            #tty.setraw(self.fd, termios.TCSANOW)
            #self.io_file = os.fdopen(self.fd, 'wb+', buffering=0)
            #flags = fcntl(self.io_file, F_GETFL)
            #fcntl(self.io_file, F_SETFL, flags | os.O_NONBLOCK)

    def thread_tty(self):
        if self.pid == pty.CHILD:
            os.execvp('bash', ['bash'])
        else:
            tty.setraw(self.fd, termios.TCSANOW)
            self.io_file = os.fdopen(self.fd, 'wb+', buffering=0)
            flags = fcntl(self.io_file, F_GETFL)
            fcntl(self.io_file, F_SETFL, flags | os.O_NONBLOCK)

    
    def _handle_string_msg(self, _, content, buffers):
        if content.get('event', '') == 'submit':
            self._submission_callbacks(self)

    def on_submit(self, callback, remove=False):
        self._submission_callbacks.register_callback(callback, remote=remove)

    def close(self):
        if not self.status:
            os.kill(self.pid, signal.SIGHUP)

    def __del__(self):
        self.close()

    #def __init__(self, **kwargs):
    #    super(HelloWorld, self).__init__(**kwargs)
    #    
    #    self.closed = False
    #    self.pid, self.fd = pty.fork()
    #    if self.pid == pty.CHILD:
    #        os.execvp('bash', ['bash'])
    #    else:
    #        tty.setraw(self.fd, termios.TCSANOW)
    #        self.file = os.fdopen(self.fd, 'wb+', buffering=0)
    #        flags = fcntl(self.file, F_GETFL)
    #        fcntl(self.file, F_SETFL, flags | os.O_NONBLOCK)
#
    #def transmit(self, data):
    #    os.write(self.fd, base64.b64decode(data))
    #    self.receive()
#
    #def receive(self):
    #    try:
    #        data = os.read(self.fd, 8192)
    #    except OSError:
    #        data = b''
    #    sys.stdout.write(base64.b64encode(data))
#
    #def update_window_size(self, rows, cols):
    #    TIOCSWINSZ = getattr(termios, 'TIOCSWINSZ', -2146929561)
    #    s = struct.pack('HHHH', rows, cols, 0, 0)
    #    ioctl(self.fd, TIOCSWINSZ, s)
    #    self.receive()
#
    #def close(self):
    #    if not self.closed:
    #        os.kill(self.pid, signal.SIGHUP)
    #
    #def __del__(self):
    #    self.close()