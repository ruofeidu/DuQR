from MyQR import myqr
import os


def generate_artistic_wifi_qr_code(ssid,
                                   password,
                                   security_type="WPA",
                                   background_image_path="logo.png",
                                   save_name="artistic_wifi_qr.png"):
  """
    生成一个带有背景图片（包含Logo）的半色调 Wi-Fi 密码 QR 码。

    Args:
        ssid (str): Wi-Fi 网络的名称 (SSID)。
        password (str): Wi-Fi 网络的密码。
        security_type (str): Wi-Fi 的安全类型（例如，"WPA", "WEP", "nopass"）。
                             默认为 "WPA"。
        background_image_path (str): 作为二维码背景的图片路径（这里假设它包含了你的Logo）。
        save_name (str): 生成的 QR 码图片文件的名称。
    """
  if not os.path.exists(background_image_path):
    print(f"错误: 找不到背景图片文件 '{background_image_path}'。请确保文件存在于当前目录。")
    print("注意: MyQR 库使用 'picture' 参数作为二维码的背景，你可以在这张背景图片中包含你的 Logo。")
    return

  # Wi-Fi QR 码的格式
  wifi_data = f"WIFI:S:{ssid};T:{security_type};P:{password};;"

  # 使用 myqr.run() 方法生成二维码
  # 'words' 是二维码中包含的数据
  # 'picture' 是背景图片（这里我们将你的 Logo 图片作为背景）
  # 'colorized' 设置为 True 可以生成半色调效果
  # 'contrast' 和 'brightness' 可以调整效果的对比度和亮度
  # 'save_name' 是生成的文件名
  # 'save_dir' 是保存文件的目录
  myqr.run(
      words=wifi_data,
      picture=background_image_path,  # 将你的 Logo 图片作为背景
      version=1,
      level='H',  # 错误纠正级别，'H' 表示高容错率
      colorized=True,  # 启用半色调效果
      contrast=1.0,  # 对比度 (0.0 - 1.0)
      brightness=1.0,  # 亮度 (0.0 - 1.0)
      save_name=save_name,
      save_dir=os.getcwd()  # 保存到当前目录
  )
  print(f"带有 Logo 的 Wi-Fi QR 码已成功生成为: {save_name}")


if __name__ == "__main__":
  # 替换为您的 Wi-Fi 网络信息
  my_ssid = input("请输入您的 Wi-Fi 网络名称 (SSID): ")
  my_password = input("请输入您的 Wi-Fi 密码: ")
  my_security_type = input(
      "请输入您的 Wi-Fi 安全类型 (例如: WPA, WEP, nopass) [默认为 WPA]: ") or "WPA"

  # 默认使用 logo.png 作为背景图片，其中包含你的 Logo
  generate_artistic_wifi_qr_code(my_ssid, my_password, my_security_type)
