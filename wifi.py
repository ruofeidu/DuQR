import qrcode


def generate_wifi_qr_code(ssid,
                          password,
                          security_type="WPA",
                          filename="wifi_qr_code.png"):
  """
    生成 Wi-Fi 密码的 QR 码。

    Args:
        ssid (str): Wi-Fi 网络的名称 (SSID)。
        password (str): Wi-Fi 网络的密码。
        security_type (str): Wi-Fi 的安全类型（例如，"WPA", "WEP", "nopass"）。
                             默认为 "WPA"。
        filename (str): 生成的 QR 码图片文件的名称。
    """
  # Wi-Fi QR 码的格式是 "WIFI:S:<SSID>;T:<TYPE>;P:<PASSWORD>;;"
  # 其中：
  # S: Wi-Fi 网络名称 (SSID)
  # T: 安全类型 (WPA, WEP, nopass)
  # P: 密码
  wifi_data = f"WIFI:S:{ssid};T:{security_type};P:{password};;"

  # 创建 QR 码实例
  qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=10,
      border=4,
  )
  qr.add_data(wifi_data)
  qr.make(fit=True)

  # 生成图片并保存
  img = qr.make_image(fill_color="black", back_color="white")
  img.save(filename)
  print(f"Wi-Fi QR 码已成功生成为: {filename}")


if __name__ == "__main__":
  # 替换为您的 Wi-Fi 网络信息
  my_ssid = input("请输入您的 Wi-Fi 网络名称 (SSID): ")
  my_password = input("请输入您的 Wi-Fi 密码: ")
  my_security_type = input(
      "请输入您的 Wi-Fi 安全类型 (例如: WPA, WEP, nopass) [默认为 WPA]: ") or "WPA"

  generate_wifi_qr_code(my_ssid, my_password, my_security_type)
