pip install tensorflow-datasets
import tensorflow_datasets as tfds


kitti, info = tfds.load("kitti", with_info=True)
