from footage_factory.config import IMAGE_FOLDER, RESULT_FOLDER
from footage_factory.footage_maker.footage_maker import FootageMaker

# 이미지를 동영상으로 만듭니다.
maker = FootageMaker(IMAGE_FOLDER, RESULT_FOLDER)
maker.process('costanza')
