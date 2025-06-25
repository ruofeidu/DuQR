# Import necessary libraries
from PIL import Image
from pyzbar.pyzbar import decode


def parse_qr_code(image_path):
  """
    Parses the content of a QR code from a given image file.

    Args:
        image_path (str): The path to the QR code image file.

    Returns:
        str: The decoded data from the QR code, or None if no QR code is found.
    """
  try:
    # Open the image file
    img = Image.open(image_path)

    # Decode QR codes from the image
    decoded_objects = decode(img)

    # Check if any QR code was found
    if decoded_objects:
      # Iterate over all decoded objects (there might be multiple QR codes)
      for obj in decoded_objects:
        # The data is in bytes, decode it to a string (e.g., utf-8)
        qr_data = obj.data.decode('utf-8')
        print(f"QR Code found! Content: {qr_data}")
        return qr_data
    else:
      print(f"No QR code found in the image: {image_path}")
      return None

  except FileNotFoundError:
    print(f"Error: Image file not found at {image_path}")
    return None
  except Exception as e:
    print(f"An error occurred: {e}")
    return None


# --- Example Usage ---
if __name__ == "__main__":
  # Specify the path to your QR code image file
  qr_image_file = "input/qr.jpg"

  # Call the function to parse the QR code
  qr_content = parse_qr_code(qr_image_file)

  if qr_content:
    print(f"\nSuccessfully parsed QR code. Content: '{qr_content}'")
  else:
    print("\nFailed to parse QR code or no QR code was found.")
