import py_compile
from pathlib import Path


def test_paper_classify_syntax():
    path = Path(__file__).with_name("paper_classify.py")
    py_compile.compile(str(path), doraise=True)
