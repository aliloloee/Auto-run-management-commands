FROM nginx:alpine
LABEL MAITAINER="Ali Loloee Jahromi"

COPY ./configuration/nginx/nginx.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]