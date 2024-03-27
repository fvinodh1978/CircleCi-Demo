
import sys

# adding src to the system path
sys.path.insert(0, '/home/circleci/circleci-python/src')
from main import add

def test_add():
    assert add(5, 1)==6
    print("Add Test : Add Function Works Correctly")

if __name__ =='__main__':
    test_add()