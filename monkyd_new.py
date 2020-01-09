#!/usr/bin/env python

import sys
import logging as log
from pymongo import MongoClient
from pkpgpdls import analyzer


# Grab the length of the document and the number of color pages
def document_get_info(filename):
    info = {"length": 0, "color": 0}

    # Run the buggy, buggy analyzer
    analyzer_info = analyzer.PDLAnalyzer(filename, analyzer.AnalyzerOptions(colorspace="gc", resolution=72))
    
    try: 
        info["length"] = analyzer_info.getJobSize()
        info["color"] = analyzer_info.getInkCoverage()[1][0]["C"]
    except(analyzer.PDLParserError):
        info["length"] = -2
    except:
        info["length"] = -1
      
    return info


# Calculate a user's quota from their group membership. 
