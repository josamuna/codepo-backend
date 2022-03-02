#!/bin/sh
# /shared-exec/start-celery-process.sh
# Script cannot be used as root user

# Specify the project directory
project_dir="codepo-backend/monitor"
# Get the current user
user=$USER
if [ user != "root" ] 
then  
	# Force kill all running celery process
    pkill celery
	# Kill celery worker if it was started with a certain PID
	# celery -A monitor multi stop worker-monitor --loglevel=INFO --pidfile="$HOME/run/celery/worker-monitor.pid" --logfile="$HOME/log/celery/worker-monitor.log"
	celery_worker_pid=`cat $HOME/run/celery/worker-monitor.pid`
	if [ ! -z $celery_worker_pid ]
	then
		# If the celery worker PID file is not null, kill also the celery worker process corresponding to the one located in the pid file
		kill $celery_worker_pid
		echo "-------`date`------------------Stop celery worker PID $celery_worker_pid-----------------------------"
	fi
	
	celery_beat_pid=`cat $HOME/run/celery/beat-monitor.pid`
	if [ ! -z $celery_beat_pid ]
	then
		# If the celery beat PID file is not null, kill also the celery worker process corresponding to the one located in the pid file
		kill $celery_beat_pid
		echo "-------`date`-------------------Stop celery beat PID: $celery_beat_pid------------------------------"
	fi

	# Change the current directory to be in the expected project directory
	cd "$(dirname $HOME/$project_dir/.)"
	# Starting celery worker task as a background task
	sleep 2s
	celery -A monitor multi start worker-monitor --loglevel=INFO --pidfile="$HOME/run/celery/worker-monitor.pid" --logfile="$HOME/log/celery/worker-monitor.log" &
	sleep 2s
	echo "*****`date`*************Celery worker started successfuly in background************************"
	
	# wait 2 seconds and then start celery beat task as a background task
	sleep 2s
	celery -A monitor beat --detach --loglevel=INFO --pidfile="$HOME/run/celery/beat-monitor.pid" --logfile="$HOME/log/celery/beat-monitor.log" &
	sleep 2s
	echo "*****`date`*************Celery beat started successfuly in background**************************"
else
    echo "You can't run this file as root user !!!"
    exit 1                                  
fi
