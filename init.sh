sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/hello.py /etc/gunicorn.d/test
sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restart