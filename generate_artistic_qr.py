from MyQR import myqr
import os
import datetime


def generate_artistic_qr_code(qr_data_text, background_image_path="image.jpg"):
  """
    生成一个带有背景图片（包含Logo）的半色调艺术二维码。

    Args:
        qr_data_text (str): QR 码中包含的文本信息。
        background_image_path (str): 作为二维码背景的图片路径。
    """
  if not os.path.exists(background_image_path):
    print(f"错误: 找不到背景图片文件 '{background_image_path}'。请确保文件存在于当前目录。")
    print("提示: MyQR 库使用 'picture' 参数作为二维码的背景。")
    return

  # 生成带日期和时间戳的文件名
  current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
  save_name = f"artistic_qrcode_{current_time}.png"

  # 使用 myqr.run() 方法生成二维码
  myqr.run(
      words=qr_data_text,
      picture=background_image_path,  # 将你的背景图片作为二维码的背景
      version=1,
      level='H',  # 高错误纠正级别，以提高可扫描性
      colorized=True,  # 启用半色调效果
      contrast=1.0,  # 对比度 (0.0 - 1.0)，可调整
      brightness=1.0,  # 亮度 (0.0 - 1.0)，可调整
      save_name=save_name,
      save_dir=os.getcwd()  # 保存到当前目录
  )
  print(f"艺术二维码已成功生成为: {save_name}")


if __name__ == "__main__":
  # 接收用户输入的 QR 码文本信息
  data_to_encode = input("请输入您希望 QR 码包含的文本信息: ")

  # 接收用户输入的背景图片路径，如果留空则使用默认的 'image.jpg'
  image_path = input("请输入背景图片路径 (默认为 'image.jpg', 直接回车使用默认): ")
  if not image_path:
    image_path = "image.jpg"

  generate_artistic_qr_code(data_to_encode, image_path)
