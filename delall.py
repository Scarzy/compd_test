#!/bin/env python

import redis

actor = redis.Redis(host='localhost',port=6379,db=0)

keys = actor.keys('*')

for i in range(len(keys)):
	actor.delete(keys[i])
