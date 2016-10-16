from nose import SkipTest

from funtests import transport


class test_qpid(transport.TransportCase):
    transport = 'qpid'
    prefix = 'qpid'

    def before_connect(self):
        try:
            import proton  # noqa
        except ImportError:
            raise SkipTest('proton Python client is not installed')
