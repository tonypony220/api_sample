SHELL = /bin/bash
img = img_fastapi
del: 
	-docker rm -f $$(docker ps | grep ${img} | cut -c1-12)
	-docker rmi $$(docker images | grep ${img} | cut -c23-37) 
b: 
	docker build -t ${img} .
run:
	docker run -p 8081:80 -dt ${img}
ex: 
	docker exec -it $$(docker ps | grep ${img} | cut -c1-12) /bin/sh
re: del b run ex
