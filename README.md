Intorduction
============

This is a simple REST api that support two endpoints. This image is based on django with python 3 and use apache as the server. This docker image consists on all the dependencies that needs to run the application. If you use jenkins configs which are provided (please refer section Building the image), it will poll the github source and build it per commit if there are any changes.

Usage and endpoints
===================

In here all the endpoints are callable through generic GET request

/msg - gives hello world message
/info - gives information about the application such as on which commit the application was built

Building the image
==================

You can build with jenkins using below configs. 
1.Make a folder in $jenkins_home/jobs/ location in disk where $jenkins_home is the home location of jenkins.
2.Download the config tar from below location
https://drive.google.com/file/d/1UDnaCBWEHIdESz0qwIm3Cvx9y6FmcCb1/view?usp=sharing
3.Untar and copy the content to the newly created folder.
4.Go to jenkins dashboard and click on "Mange Jenkins".
5.Click and reload the configs by using "Reload Configuration from Disk" option.
6.Go to newly created project and click "Build Now"

You can manualy build the docker container using below steps
1.Clone the repo using below command
git clone https://github.com/LolithaRatnayake/myob_testApi.git
2.cd into the repo using below command
cd myob_testApi/
3.Run below command to build the container
docker build -f Dockerfile . -t test --build-arg commit=$(git rev-parse HEAD)


Running the docker image
========================

Pre-request
----------

1.Install docker on machine you want to run.
refer : https://docs.docker.com/install/

Running
-------

If you build the docker image manually
1.Then you can proceed by running below command
docker run test
2.It will show up the ip address which the container is running at the prompt

However if you used jenkins
1.Then go to last build
2.Go to "Last Successful Artifacts"
3.Download testApi.tar
4.Load the image to system using below command
docker load < testApi.tar

