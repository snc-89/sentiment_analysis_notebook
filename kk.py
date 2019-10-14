#!/usr/bin/python

import httplib2
import os
import sys
import csv
from googleapiclient.discovery import build
from apiclient.errors import HttpError
import json
import test

playListIDs = ['PLk1Sqn_f33KvtMA4mCQSnzGsZe8qsTdzV',
               'PLk1Sqn_f33Kvv8T6ZESpJ2nvEHT9xBhlb',
               'PLk1Sqn_f33KtVQWWnE_V6-sypm5zUMkU6',
               'PLk1Sqn_f33KuU_aJDvMPPAy_SoxXTt_ub',
               'PLk1Sqn_f33Ku0Oa3t8MQjV7D_G_PBi8g1',
               'PLk1Sqn_f33KvXucAFMo5Tc5p8e_mcc-5g',
               'PLk1Sqn_f33KtYIPnFjpI19BCz2unzWYlJ',
               'PLk1Sqn_f33KuQyLE4RjEOdJ_-0epbcBb4']

items1 = test.playlistItems(playListIDs[0],6)
items2 = test.playlistItems(playListIDs[1],3)
items3 = test.playlistItems(playListIDs[2],5)
items4 = test.playlistItems(playListIDs[3],7)
items5 = test.playlistItems(playListIDs[4],5)
items6 = test.playlistItems(playListIDs[5],4)
items7 = test.playlistItems(playListIDs[6],2)
items8 = test.playlistItems(playListIDs[6],2)

joinedItems = items1+items2+items3+items4+items5+items6+items7+items8


IDs = test.getIDs(joinedItems)
print(len(IDs))
with open('vidIDs.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(IDs)
myfile.close()



