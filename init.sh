rm /etc/nginx/sites-enabled/default
ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
ln -s /home/box/web/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/nginx restart
