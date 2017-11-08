#!/usr/bin/env python
# -*- coding: utf-8 -*-
import angr
import logging

#logging.basicConfig(level=logging.DEBUG)

proj = angr.Project('./tmp', load_options={'auto_load_libs':False})
target = 0x400a07
 
ex = proj.surveyors.Explorer(find=(target,),avoid=(0x400a18,),enable_veritesting=True)
ex.run()
payload = ''
if ex.found:
    payload = ex.found[0].state.posix.dumps(0)
    print "DILDO!"
    print payload
    print "DILDO!"
