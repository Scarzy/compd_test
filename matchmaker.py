#!/bin/env python

import redis
from random import choice

teams = ['ARG','BWS','BWS2','BGR','BRK','BSG','CLF','CLF2','EMM','GRS','GMR','HRS','HZW','MFG','MUC','PSC','PSC2','QEH','QMC','SEN','SEN2','TTN']
matches = ["3600,PSC,MFG,BSG,QMC,1"]

actor = redis.Redis(host='localhost',port=6379,db=0)

for i in range(20):
	str = '{0},{1},{2},{3},{4},{5}'.format((3600 + (7*(i+1))),choice(teams),choice(teams),choice(teams),choice(teams),i+2)
	matches.append(str)

for i in range(21):
	print(matches[i])
	actor.rpush('org.srobo.matches',matches[i])
