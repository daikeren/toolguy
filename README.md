# build
docker build . -t toolguy
# start
docker run -d -p 8000:8000 --name toolguy toolguy
# stop
docker stop toolguy
