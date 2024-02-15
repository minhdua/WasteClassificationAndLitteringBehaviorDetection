import os
import cv2
import numpy as np

def resize_image(image, target_size):
    """
    Resize một hình ảnh đến kích thước mong muốn.

    :param image: Hình ảnh cần resize.
    :param target_size: Kích thước đích.
    :return: Hình ảnh sau khi resize.
    """
    return cv2.resize(image, target_size)

def augment_image(image):
    """
    Tăng cường hình ảnh (ví dụ: xoay, phản chiếu).

    :param image: Hình ảnh cần tăng cường.
    :return: Hình ảnh sau khi tăng cường.
    """
    # Xoay hình ảnh
    image_rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    
    # Phản chiếu hình ảnh
    image_flipped = cv2.flip(image, 1)
    
    return image_rotated, image_flipped

def process_image(file_path, target_size=(224, 224)):
    """
    Tiền xử lý hình ảnh bao gồm resize và tăng cường.

    :param file_path: Đường dẫn đến file hình ảnh.
    :param target_size: Kích thước đích cho việc resize.
    :return: Hình ảnh sau khi tiền xử lý.
    """
    image = cv2.imread(file_path)
    image_resized = resize_image(image, target_size)
    image_augmented = augment_image(image_resized)
    return image_resized, image_augmented

def main():
    image_directory = '../data/images/training'  # Thay thế bằng đường dẫn thực tế
    processed_directory = '../data/images/processed'  # Thay thế bằng đường dẫn lưu hình ảnh sau khi xử lý

    for filename in os.listdir(image_directory):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            file_path = os.path.join(image_directory, filename)
            image_resized, image_augmented = process_image(file_path)
            
            # Lưu hình ảnh đã tiền xử lý
            cv2.imwrite(os.path.join(processed_directory, 'resized_' + filename), image_resized)
            cv2.imwrite(os.path.join(processed_directory, 'augmented_' + filename), image_augmented[0])
            cv2.imwrite(os.path.join(processed_directory, 'augmented_flipped_' + filename), image_augmented[1])

if __name__ == '__main__':
    main()
