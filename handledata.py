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
    #copy_directory("./data/mvtec/"+ c.class_name + "/test/defective", "./dataset/"+ c.class_name + "/test/anomaly")
    #copy_directory("./data/mvtec/"+ c.class_name + "/test/crack", "./dataset/"+ c.class_name + "/test/anomaly")
    #copy_directory("./data/mvtec/"+ c.class_name + "/test/faulty_imprint", "./dataset/"+ c.class_name + "/test/anomaly")
    #copy_directory("./data/mvtec/"+ c.class_name + "/test/poke", "./dataset/"+ c.class_name + "/test/anomaly")
    #copy_directory("./data/mvtec/"+ c.class_name + "/test/scratch", "./dataset/"+ c.class_name + "/test/anomaly")
    #copy_directory("./data/mvtec/"+ c.class_name + "/test/squeeze", "./dataset/"+ c.class_name + "/test/anomaly")
    copy_directory("./data/mvtec/"+ c.class_name + "/test/bent", "./dataset/"+ c.class_name + "/test/anomaly")
    copy_directory("./data/mvtec/"+ c.class_name + "/test/broken", "./dataset/"+ c.class_name + "/test/anomaly")
    copy_directory("./data/mvtec/"+ c.class_name + "/test/glue", "./dataset/"+ c.class_name + "/test/anomaly")
    copy_directory("./data/mvtec/"+ c.class_name + "/test/metal_contamination", "./dataset/"+ c.class_name + "/test/anomaly")
    copy_directory("./data/mvtec/"+ c.class_name + "/test/thread", "./dataset/"+ c.class_name + "/test/anomaly")



def copy_directory(fromDirectory, toDirectory):
    copy_tree(fromDirectory, toDirectory)