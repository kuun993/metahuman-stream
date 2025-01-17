###############################################################################
# 仅支持openai调用方式的一些平台
###############################################################################


from enum import Enum
class LLMProvider(Enum):
    OPENAI = "openai"
    AZURE = "azure"
    QWEN = "qwen"
    DEEPSEEK = "deepseek"
