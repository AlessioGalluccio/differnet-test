from pathlib import Path
from distutils.dir_util import copy_tree
import config as c

def handledata():
    Path("./dataset/"+ c.class_name).mkdir(parents=True, exist_ok=True)
    Path("./dataset/"+ c.class_name + "/train").mkdir(parents=True, exist_ok=True)
    Path("./dataset/"+ c.class_name + "/test").mkdir(parents=True, exist_ok=True)
    Path("./dataset/"+ c.class_name + "/train/good").mkdir(parents=True, exist_ok=True)
    Path("./dataset/"+ c.class_name + "/test/anomaly").mkdir(parents=True, exist_ok=True)
    Path("./dataset/"+ c.class_name + "/test/good").mkdir(parents=True, exist_ok=True)

    copy_directory("./data/mvtec/"+ c.class_name + "/train/good", "./dataset/"+ c.class_name + "/train/good")
    copy_directory("./data/mvtec/"+ c.class_name + "/test/good", "./dataset/"+ c.class_name + "/test/good")
    copy_directory("./data/mvtec/"+ c.class_name + "/test/defective", "./dataset/"+ c.class_name + "/test/anomaly")



def copy_directory(fromDirectory, toDirectory):
    copy_tree(fromDirectory, toDirectory)