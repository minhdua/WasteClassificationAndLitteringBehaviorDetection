from src.models.classification_model import train_classification_model
from src.models.detection_model import train_detection_model

def train_models(image_data_dir, video_data_dir, model_save_dir):
    # Huấn luyện mô hình phân loại rác thải
    print("Huấn luyện mô hình phân loại rác thải...")
    train_classification_model(image_data_dir, model_save_dir)

    # Huấn luyện mô hình phát hiện hành vi vứt rác
    print("Huấn luyện mô hình phát hiện hành vi vứt rác...")
    train_detection_model(video_data_dir, model_save_dir)

if __name__ == "__main__":
    image_data_dir = 'data/images/processed/'
    video_data_dir = 'data/videos/processed/'
    model_save_dir = 'models/'

    train_models(image_data_dir, video_data_dir, model_save_dir)
