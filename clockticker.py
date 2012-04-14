#!/bin/env python

import redis
from time import sleep, time
from math import floor

actor = redis.Redis(host='localhost',port=6379,db=0)

while True:
	actor.incr('org.srobo.time.competition',1)
	actor.set('org.srobo.time.real',floor(time()))
	sleep(1)
