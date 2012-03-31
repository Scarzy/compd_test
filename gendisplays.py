#!/bin/env python

import redis
from decimal import Decimal

actor = redis.Redis(host='localhost',port=6379,db=0)

actor.zadd('org.srobo.displays.screens','zone0',1)
actor.zadd('org.srobo.displays.screens','zone1',2)
actor.zadd('org.srobo.displays.screens','zone2',3)
actor.zadd('org.srobo.displays.screens','zone3',4)
actor.zadd('org.srobo.displays.screens','door',5)

