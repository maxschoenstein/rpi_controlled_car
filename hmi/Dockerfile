FROM nginx

COPY ./nginx-1.25.3/conf/nginx.conf /etc/nginx/conf/nginx.conf
COPY ./nginx-1.25.3/html/index.html /etc/nginx/html/index.html


CMD ["nginx", "-g", "daemon off;"]