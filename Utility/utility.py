
"""utils.py"""

import argparse
import os
import subprocess

import torch
import torch.nn as nn
from torch.autograd import Variable
from torchvision.utils import save_image
import numpy as np
from torchvision.datasets import ImageFolder 
from torch.utils.data import DataLoader

def str2bool(v):
    # codes from : https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse

    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')
    
def get_number(name):
    name = name.split('.')[0]
    try:
        name = int(name)
    except:
        pass
    return name