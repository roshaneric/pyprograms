run-local:
	python helloworld.py

build-image:
	docker build -t hellopy:roshanf .

run-image:
	docker run --env USERNAME=roshanf hellopy

list-containers:
	docker ps -a

rm-stopped:
	docker rm $$(docker ps -a -q)

create-cronjob:
	kubectl create -f pycronjob.yaml

get-cronjob:
	kubectl get cronjob hellopyjob

watch:
	kubectl get jobs --watch

delete:
	kubectl delete cronjob hellopyjob

