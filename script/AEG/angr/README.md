* `docker run -d -t --ulimit='stack=-1:-1' --name angr -v <working_dir>:/home/angr/work/ angr/angr` to run angr in background
* `docker exec -it angr su angr` to get in
* `source /usr/share/virtualenvwrapper/virtualenvwrapper.sh` && `workon angr`
* `cd /home/angr/work`, start working
