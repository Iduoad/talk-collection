---
title: Bringing back dial-up:the internet over SMS
description: building a browser that makes all requests over SMS 
type: talk
speaker: Alexandra Sunderland   
source: //www.youtube.com/watch?v=ZsBAkSxwU5c&list=PL37ZVnwpeshHwJPVBqEnZild7QHWhdufu&index=17
tag : ['Javascript','node.js']
---
- Problem: Internet access is so expensive in some countries 
- 1st approach: setting up a python server that would grab the data from internet and send it back via SMS
- 2nd approach: Build a browser(an android app,Twilio as a endpoint to send SMS to , Node.Js server)
- challenges:SMS only handle 160 characters at a time
- We get rid of all the unnecessary data(css ,header data,comments..)
- replace long links with short links  
