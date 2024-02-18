import os
import pdb
import numpy as np
import cv2

import shutil

def move_images(source_directory, destination_directory):
  """
  Di chuyển tất cả hình ảnh từ thư mục nguồn sang thư mục đích.

  :param source_directory: Thư mục chứa hình ảnh nguồn.
  :param destination_directory: Thư mục đích.
  """
  for item in os.listdir(source_directory):
        shutil.move(os.path.join(source_directory, item), destination_directory)


def load_images(directory):
  """
  Tải tất cả hình ảnh trong thư mục và các thư mục con của nó.

  :param directory: Thư mục chứa hình ảnh.
  :return: Danh sách các mảng NumPy chứa dữ liệu hình ảnh.
  """
  images = []
  for root, dirs, files in os.walk(directory):
    for file in files:
      if file.endswith('.jpg') or file.endswith('.png'):
        image = cv2.imread(os.path.join(root, file))
        images.append(image)
    for dir in dirs:
      sub_dir = os.path.join(root, dir)
      images.extend(load_images(sub_dir))
  return images

def load_labels(file_path):
  """
  Tải các nhãn từ file.

  :param file_path: Đường dẫn đến file chứa nhãn.
  :return: Danh sách các nhãn.
  """
  labels = []
  with open(file_path, 'r') as f:
    for line in f:
      labels.append(line.strip())
  return labels

def split_dataset(images, labels, train_ratio=0.8, validation_ratio=0.1):
  """
  Chia tập dữ liệu thành tập huấn luyện, tập xác thực và tập kiểm tra.

  :param images: Danh sách các mảng NumPy chứa dữ liệu hình ảnh.
  :param labels: Danh sách các nhãn.
  :param train_ratio: Tỷ lệ tập huấn luyện.
  :param validation_ratio: Tỷ lệ tập xác thực.
  :return: Tuple chứa (images_train, labels_train, images_validation, labels_validation, images_test, labels_test).
  """
  pdb.set_trace()
  num_samples = len(images)

  # Chia tập dữ liệu
  train_size = int(num_samples * train_ratio)
  validation_size = int(num_samples * validation_ratio)
  test_size = num_samples - train_size - validation_size

  images_train = images[:train_size]
  labels_train = labels[:train_size]

  images_validation = images[train_size:train_size + validation_size]
  labels_validation = labels[train_size:train_size + validation_size]

  images_test = images[train_size + validation_size:]
  labels_test = labels[train_size + validation_size:]

  return images_train, labels_train, images_validation, labels_validation, images_test, labels_test

def main():
  # Di chuyển hình ảnh
  move_images('data/images/processed', 'data/images/training')

  # Tải dữ liệu
  images = load_images('data/images/')
  # labels = load_labels('labels/image_labels')
  labels = ['inorganic', 'organic']

  # Chia tập dữ liệu
  images_train, labels_train, images_validation, labels_validation, images_test, labels_test = split_dataset(images, labels)

  # In thông tin
  print(f"Số lượng ảnh huấn luyện: {len(images_train)}")
  print(f"Số lượng ảnh xác thực: {len(images_validation)}")
  print(f"Số lượng ảnh kiểm tra: {len(images_test)}")


if __name__ == "__main__":
  main()


