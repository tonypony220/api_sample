all:
	docker-compose up 
b:
	docker-compose build 
deldata:
	docker-compose down --volumes
	docker volume rm $$(docker volume ls -q)
cl: 
	docker rmi -f $$(docker images --filter "dangling=true" -q)
prune: 
	docker system prune
	docker rmi -f $$(docker images -aq)
	-docker network prune -f
	-docker rmi -f $$(docker images --filter dangling=true -qa)
	-docker volume rm $$(docker volume ls --filter dangling=true -q)
	-docker rmi -f $$(docker images -qa)
	
