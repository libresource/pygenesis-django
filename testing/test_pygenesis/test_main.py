"""
Test main
"""
from pygenesis import info


def test_info():
    """
    Test info
    :return: None
    """
    info_expected_text = ('Just use this GitHub repository as template: '
                          'https://github.com/libresource/pygenesis and enjoy yourself')
    assert info() == info_expected_text
