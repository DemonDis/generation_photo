import os
from PIL import Image
from src.image_processor import process_image_with_api
from src.config import INPUT_DIR, OUTPUT_DIR

def main():
    # Проверка и создание директорий
    if not os.path.exists(INPUT_DIR):
        print(f"Входная директория '{INPUT_DIR}' не найдена. Пожалуйста, создайте ее и поместите изображения.")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Обработка изображений
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            input_image_path = os.path.join(INPUT_DIR, filename)
            output_image_path = os.path.join(OUTPUT_DIR, f"processed_{filename}")
            process_image_with_api(input_image_path, output_image_path)
        else:
            print(f"Пропущен файл {filename} (не поддерживаемый формат изображения).")

if __name__ == "__main__":
    main()
