FROM cloudera/quickstart
COPY twitterstream.py twitterstream.py
COPY get-pip.py get-pip.py
COPY files/* files/
COPY app.sh app.sh
RUN python get-pip.py
RUN pip install oauth2
RUN pip install mysql-connector==2.1.4
RUN python twitterstream.py 500 431072615-myG4gQQzgXtE9BurVmyA5mVr3dNKWZxdEZPbN8IY zC71vA4Oc8zT6ugHuZIZ7roNkUvxYbThxOOuHRa5DIIlO pO3LCNowlQbljfas3cf1P16t3 LU0FChqGxZl2zOKpOEKIek8pUtiesgg2iiRAZF1cm1SmtahwbJ > datos.txt
