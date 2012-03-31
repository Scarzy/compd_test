#!/bin/env python

import random, redis

teams = ['ARG','BWS','BWS2','BGR','BRK','BSG','CLF','CLF2','EMM','GRS','GMR','HRS','HZW','MFG','MUC','PSC','PSC2','QEH','QMC','SEN','SEN2','TTN']

actor = redis.Redis(host='localhost',port=6379,db=0)

def game_points(score):
        total = 0
        total += int(score[2])
        total += 2*int(score[3])
        total += 5*int(score[4])
        if int(score[5]) > 1:
                total *= int(score[5])
        return total

for i in range(21):
	for j in range(4):
		r = int(random.random()*10)
		z = int(random.random()*10)
		b = int(random.random()*10)
		n = int(random.random()*10)%5
		s = game_points([0,0,r,z,b,n])
		actor.hmset('org.srobo.scores.match.{0}.{1}'.format(i,j),{'trobot':r,'tzone':z,'tbucket':b,'nbuckets':n})
	actor.incr('org.srobo.scores.team.{0}'.format(teams[i]),s)
