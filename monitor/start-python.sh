#!bin/bash
# Specify the project directory
project_dir="codepo-backend/monitor"
cd "$(dirname $HOME/$project_dir/.)"

echo "******************************************************************************************************"
echo "********`date`****************START PYTHON TASK*********************************"
python3 $HOME/$project_dir/manage.py gunicorn --bind 0.0.0.0:8000 >> "$HOME/log/python/python-monitor.log" 2>&1 &
echo "*********************************************SUCCESSFULY STARTED**************************************"
