# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-09-04 23:19:03
# @Last Modified by:   jankincai12@gmail.com
# @Last Modified time: 2019-09-24 09:49:13
import os


def to_c_str(v):
    """
    Python str to C str
    """

    try:
        return v.encode("utf-8")
    except Exception:
        pass

    return b""


def from_c_str(v):
    """
    C str to Python str
    """

    try:
        return v.decode("utf-8")
    except Exception:
        pass

    return ""


def get_pcap_file(path):
    """
    get pcap file

    :param path: path.
    """

    if isinstance(path, bytes):
        path = from_c_str(path)

    return (
        os.path.join(directory, file)
        for directory, dirs, files in os.walk(path)
        for file in files if ".pcap" in file
    )
