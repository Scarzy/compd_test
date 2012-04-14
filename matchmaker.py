#!/bin/env python

import redis, json
from random import choice

teams = ['ARG','BWS','BWS2','BGR','BRK','BSG','CLF','CLF2','EMM','GRS','GMR','HRS','HZW','MFG','MUC','PSC','PSC2','QEH','QMC','SEN','SEN2','TTN']
matches = ["{'time':3600,'teams': ['PSC','MFG','BSG','QMC'], 'delay': 1}"]

actor = redis.Redis(host='localhost',port=6379,db=0)

for i in range(20):
	obj = {'time': (3600 + (7*60*(i+1))),'teams':[choice(teams),choice(teams),choice(teams),choice(teams)],'delay':3}
	str = json.dumps(obj)
	matches.append(str)

for i in range(21):
	print(matches[i])
	actor.rpush('org.srobo.matches',matches[i])
