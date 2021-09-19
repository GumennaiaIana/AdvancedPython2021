#!/bin/bash
cd  ~
touch info.txt
date>info.txt
whoami>>info.txt
uname>>info.txt
ls -l|grep ^d|wc -l>>info.txt
ls -lR|grep "^-"|wc -l>>info.txt
