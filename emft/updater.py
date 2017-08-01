# coding=utf-8

from emft.__version__ import __version__
from emft.utils.updater import Updater, Channel
from emft.cfg import Config

updater = Updater(
    current_version=__version__,
    av_user='132nd-etcher',
    av_repo='EMFT',
    local_executable='emft.exe',
    channel=Channel.LABEL_TO_CHANNEL[Config().update_channel],
)