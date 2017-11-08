all: pull run

pull:
	docker pull angr/angr
run:
	docker run -it angr/angr
bash:
	docker run -e TERM --privileged --security-opt seccomp:unconfined -v /home/bruce30262/angr/work:/home/angr/work --name=angr -it angr/angr /bin/bash
exec:
	docker exec -it angr /bin/bash
