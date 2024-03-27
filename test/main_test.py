
import sys

# adding src to the system path
sys.path.insert(0, '/home/circleci/circleci-python/src')
from main import add, product

def test_add():
    assert add(5, 5)==10
    print("Add Test : Add Function Works Correctly")

def test_product():
    assert product(5, 5)==25
    print("Add Test : product Function Works Correctly")

if __name__ =='__main__':
    test_add()
    test_product()