#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: baoyi
# Datetime: 2021/4/9 16:04
import os
import base64


def get_geojson_file_downloader_html(data, name='data', file_label='File'):
    """
    下载本地文件
    st.markdown(get_binary_file_downloader_html('photo.jpg', 'Picture'), unsafe_allow_html=True)
    :param name:
    :param data:
    :param file_label:
    :return:
    """
    bin_str = base64.b64encode(data.encode()).decode()
    href = f'<a href="data:application/json;base64,{bin_str}" download="{name}.geojson">Download {file_label}</a> '
    return href
