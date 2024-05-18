from gedcom.element.element import Element
from gedcom.element.file import FileElement
import gedcom.tags


def test_initialization():
    file_element = FileElement(level=-1, pointer="", tag=gedcom.tags.GEDCOM_TAG_FILE, value="")
    assert isinstance(file_element, Element)
    assert isinstance(file_element, FileElement)
