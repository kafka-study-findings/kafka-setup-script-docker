#!/bin/bash

docker exec -it kafka-setup-script-docker-broker-1 kafka-console-producer --bootstrap-server localhost:29092 --topic test
