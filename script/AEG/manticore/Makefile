all: pull run

pull:
	docker pull japesinator/manticore
run:
	docker run -e TERM --privileged --security-opt seccomp:unconfined -v /home/bruce30262/manticore/work:/home/manticore/work --name=manticore -it japesinator/manticore /bin/bash
exec:
	docker exec -it manticore /bin/bash
