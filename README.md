Manual

1. git clone < this repository >
2. sudo docker build .
3. sudo docker run -p 8000:8000 f265d17a56f3 (your IMAGE)
4. Check server run - http://localhost:8000/status/
5. sudo docker ps - show your CONTAINER information
6. sudo docker rm -f a1e7f05c37c8 (your CONTAINER ID) - delete container from another terminal if command Ctrl+C doesn't work!
