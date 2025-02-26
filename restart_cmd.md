ps aux | grep gunicorn
kill <PID>
gunicorn -w 4 -b 127.0.0.1:5000 app:app