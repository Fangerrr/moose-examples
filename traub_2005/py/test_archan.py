# test_archan.py --- 
# 
# Filename: test_archan.py
# Description: 
# Author: 
# Maintainer: 
# Created: Sat Jun  2 11:05:22 2012 (+0530)
# Version: 
# Last-Updated: Sun Jun 25 16:19:47 2017 (-0400)
#           By: subha
#     Update #: 8
# URL: 
# Keywords: 
# Compatibility: 
# 
# 

# Commentary: 
# 
# 
# 
# 

# Change log:
# 
# 
# 

# Code:


import numpy as np
import testutils
from testutils import *
from archan import *
from channel_test_util import compare_channel_data, run_single_channel, ChannelTestBase

simtime = 350e-3
simdt = testutils.SIMDT
plotdt = testutils.PLOTDT

class TestAR(ChannelTestBase):
    channelname = 'AR'
    params = run_single_channel(channelname, 1e-9, simtime)
    vm = np.array(params['Vm'].vector)
    gk = np.array(params['Gk'].vector)
    tseries = np.arange(0, len(vm), 1.0) * simdt
    
    def testAR_Vm_Neuron(self):
        data = np.c_[self.tseries, self.vm]
        try:
            err = compare_channel_data(data, self.channelname, 'Vm', 'neuron', x_range=(simtime/10.0, simtime))
            self.assertLess(err, 0.01)
        except IOError:
            print('Could not find NRN data')

    def testAR_Gk_Neuron(self):
        data = np.c_[self.tseries, self.gk]
        try:
            err = compare_channel_data(data, self.channelname, 'Gk', 'neuron', x_range=(simtime/10.0, simtime), plot=True)
            self.assertLess(err, 0.01)
        except IOError:
            print('Could not find NRN data')


if __name__ == '__main__':
    unittest.main()

# 
# test_archan.py ends here
