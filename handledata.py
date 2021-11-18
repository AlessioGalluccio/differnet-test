from pathlib import Path
from distutils.dir_util import copy_tree

def handledata():
    Path("./dataset/toothbrush").mkdir(parents=True, exist_ok=True)
    Path("./dataset/toothbrush/train").mkdir(parents=True, exist_ok=True)
    Path("./dataset/toothbrush/test").mkdir(parents=True, exist_ok=True)
    Path("./dataset/toothbrush/train/good").mkdir(parents=True, exist_ok=True)
    Path("./dataset/toothbrush/test/anomaly").mkdir(parents=True, exist_ok=True)
    Path("./dataset/toothbrush/test/good").mkdir(parents=True, exist_ok=True)

    copy_directory("./data/mvtec/toothbrush/train/good", "./dataset/toothbrush/train/good")
    copy_directory("./data/mvtec/toothbrush/test/good", "./dataset/toothbrush/test/good")
    copy_directory("./data/mvtec/toothbrush/test/defective", "./dataset/toothbrush/test/anomaly")



def copy_directory(fromDirectory, toDirectory):
    copy_tree(fromDirectory, toDirectory)