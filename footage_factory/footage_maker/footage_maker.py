import os
import cv2
import time

class FootageMaker:

    def __init__(self, image_dir, result_dir):
        self.image_dir = image_dir
        self.result_dir = result_dir
        pass


    def process(self, dir_name):
        working_dir = os.path.join(self.image_dir, dir_name)

        for file_name in os.listdir(working_dir):
            file_name = os.path.join(working_dir, file_name)
            image = cv2.imread(file_name)
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imshow("Over the Clouds", image)
            cv2.imshow('hihi', gray_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        print('작업 완료')
