
import textwrap
from .utils import PreprocessorTest
from .test_processor_rst import RSTPreprocessorTest
from .test_processor_google import GooglePreprocessorTest
from pydocmk2.preprocessors.smart import Preprocessor


class SmartRSTPreprocessorTest(RSTPreprocessorTest):
    preprocessor = Preprocessor()


class SmartGooglePreprocessorTest(GooglePreprocessorTest):
    preprocessor = Preprocessor()
