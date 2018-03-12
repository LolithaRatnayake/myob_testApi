FROM ubuntu

ARG commit

RUN apt-get update
RUN apt-get install -y apt-utils apache2 apache2-utils
#RUN apt-get -y install libapache2-mod-wsgi-py3
RUN apt-get -y install python3 libapache2-mod-wsgi-py3
RUN ln /usr/bin/python3 /usr/bin/python
RUN apt-get -y install python3-pip
RUN apt-get -y install sqlite3
RUN ln /usr/bin/pip3 /usr/bin/pip
RUN pip install --upgrade pip
ADD ./requests.txt /home/requests.txt
RUN pip install -r /home/requests.txt
ADD ./testApi.conf /etc/apache2/sites-available/000-default.conf
ADD ./testApi/ /var/www/html/testApi/
#RUN python /var/www/html/testApi/manage.py dbshell <<EOF \
#    update testapp_info set lastcommitsha=\"$commit\"; \
#    EOF
ADD ./updatedb.sh /home/updatedb.sh
RUN /home/updatedb.sh $commit
RUN rm -rf /var/www/html/index.html
EXPOSE 80 3500
CMD ["apache2ctl", "-D", "FOREGROUND"]
