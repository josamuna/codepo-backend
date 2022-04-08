#!/bin/bash

echo 'Use this PID to kill celery process: '
pid_file="run/celery/worker-monitor.pid"
cat "$(dirname $HOME/$pid_file/.)"
echo 'Type celery PID to kill celery process : '
read celery_pid

if [ ! -z $celery_pid ]
then
	pkill celery
	sleep 1s
	kill $celery_pid
	echo "*******Celery process pid killed successfully on *** `date`*********"
fi	

