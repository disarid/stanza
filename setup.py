__author__ = 'victor'

from distutils.core import setup, Command


class UnitTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        errno = subprocess.call(['python', '-m', 'unittest', 'discover', 'stanza/test/unit_tests'])
        raise SystemExit(errno)

class SlowTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        errno = subprocess.call(['python', '-m', 'unittest', 'discover', 'stanza/test/slow_tests'])
        raise SystemExit(errno)

setup(
    name='stanza',
    version='0.1',
    packages=['stanza', 'stanza.text', 'stanza.util'],
    url='https://github.com/stanfordnlp/stanza',
    license='MIT',
    author='Stanford NLP',
    author_email='victor@victorzhong.com',
    description='NLP library for Python',
    cmdclass={'test': UnitTest, 'slow_test': SlowTest},
    download_url='https://github.com/stanfordnlp/stanza/tarball/0.1',
    keywords=['nlp', 'neural networks', 'machine learning'],
)