import os
from businessView.tools import *

import pytest

if __name__ == '__main__':

    for i in os.listdir(TEST_PATH):
        if i.startswith('IMP') == True:
            pytest.main(["-v", "-s", f"%s{i}" % TEST_PATH, "--alluredir=%s" % REPORT_PATH])
