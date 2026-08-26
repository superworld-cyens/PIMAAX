import sys
import os

#userdefined class
from core.utils import Configuration
from core import PiMaax


if __name__ == "__main__":
    config = Configuration("/home/chirag/pimaax-firmware/config/config.yaml") #take yaml/json and convert to iter Dict

    #initialize the controller and run
    controller = PiMaax(config)
    controller.run()