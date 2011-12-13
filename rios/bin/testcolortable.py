"""
A simple test of color-table funcionality

Creates a raster image, and adds a color table to it. Then
reads it back, and checks that we get the same thing we
put there. 

"""
import os
import numpy

from rios import rat

import riostestutils

TESTNAME = "TESTCOLORTABLE"

def run():
    """
    Run the color table test
    """
    riostestutils.reportStart(TESTNAME)
    
    filename = 'test.img'
    ds = riostestutils.genThematicFile(filename)
    del ds
    
    clrTbl = numpy.array([
        [0, 0, 0, 0, 0],
        [1, 255, 0, 0, 0],
        [2, 0, 255, 0, 0],
        [3, 0, 0, 255, 0],
    ], dtype=numpy.uint8)

    rat.setColorTable(filename, clrTbl)
    clrTbl2 = rat.getColorTable(filename)
    
    # Check the first N rows of the color table. This assumes
    # that we gave contiguous values in the input table (which we did)
    n = len(clrTbl)
    if (clrTbl == clrTbl2[:n]).all():
        riostestutils.report(TESTNAME, 'Passed')
    else:
        riostestutils.report(TESTNAME, 'Retrieved color table not equal to that written')

    os.remove(filename)