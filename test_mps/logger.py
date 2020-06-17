#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Huang Fulin
@filename: logger.py
@date: 2019/9/24 
"""

import logging
fmt = "%(asctime)-15s [%(levelname)s] %(filename)s %(lineno)d %(message)s"
logging.basicConfig(format=fmt, level=logging.DEBUG)
logger = logging.getLogger('test_mps')