class ImageHandler:
    def __init__(self, driver):
        self.driver = driver
    
    def upload_image(self, locator, file_path):
        self.driver.find_element(*locator).send_keys(file_path)

# Example usage:
# image_upload_locator = (By.ID, 'image_upload_id')
# image_handler = ImageHandler(driver)
# image_handler.upload_image(image_upload_locator, 'path_to_image.jpg')
