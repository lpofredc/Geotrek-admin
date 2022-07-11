FROM geotrekce/admin:2.29.13

RUN groupmod -g 1000 django && \
    usermod -u 1000 -g 1000 django

RUN find /app/src -uid 2000 -exec chown -v -h 1000:1000 '{}' \; 
# find / -gid 2000 -exec chgrp -v -h 1000 '{}' \;


ENTRYPOINT ["/bin/bash", "-e", "/usr/local/bin/entrypoint.sh"]
# CMD ["./manage.py", "runserver", "0.0.0.0:8000"]
CMD ["echo","$(whoami)","whoami"]

