from abc import ABCMeta, abstractproperty
from rest_framework import status

class ShrimpException(Exception, metaclass=ABCMeta):
    errors = None
    def __init__(self, errors=None):
        super.__init__(self.message)
        self.errors = errors

    @abstractproperty
    def code(self):
        pass

    @abstractproperty
    def message(self):
        pass


class NotExistFileException(ShrimpException):
    @property
    def code(self):
        return status.HTTP_400_BAD_REQUEST

    @property
    def message(self):
        return "파일을 업로드 해주십시오."


class NotSupportFormatException(ShrimpException):
    @property
    def code(self):
        return status.HTTP_400_BAD_REQUEST

    @property
    def message(self):
        return "지원하지 않는 영상 포맷입니다."


class ProcessFailException(ShrimpException):
    @property
    def code(self):
        return status.HTTP_400_BAD_REQUEST

    @property
    def message(self):
        return "파일 필터링이 실패하였습니다."
        

class LoadModelFailException(ShrimpException):
    @property
    def code(self):
        return status.HTTP_400_BAD_REQUEST

    @property
    def message(self):
        return "학습된 모델을 로드하지 못했습니다."