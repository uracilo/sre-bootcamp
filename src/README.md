# Implementation Checklist
- [x] API Code
- [x] Services Code
- [x] Unit-tests
- [x] Dockerfile
- [x] It Compiles
- [x] It runs

# Api Services
- Receives a valid username and password and returns a JWT.
- Returns protected data with a valid token, otherwise returns unauthenticated.


# Image 

You can view the image of the proyect on: 

https://hub.docker.com/repository/docker/uracilo/wize-benjamin-casazza


# Image  for unit test
```

docker build  -f Dockerfiles/Dockerfile.test -t wize-test .
docker run -it wize-test 
```

# Image for dev
```

docker build  -f Dockerfiles/Dockerfile.dev -t wize-dev .
docker run -itd wize-dev  -p 8080:8000
```

# Check the responses 

```

http post host:8000/login username=test password=test
export JWT=TOKEN
echo $JWT
http post host:8000/protected Authorization:"Bearer $JWT"
http get host:8000/protected Authorization:"Bearer $JWT"

```
