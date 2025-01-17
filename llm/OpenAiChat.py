###############################################################################
# openai 接口
###############################################################################

from abc import ABCMeta, abstractmethod

class IOpenAiChat(metaclass = ABCMeta):

    @abstractmethod
    def chat(prompt: str):
        pass

    @abstractmethod
    def chat(system_prompt: str, user_massage: str):
        pass




