#!/bin/bash

docker exec -it kafka-setup-script-docker-broker-1 \
	kafka-console-consumer \
	--bootstrap-server localhost:29092 \
	--property print.key=true \
	--topic test --from-beginning
