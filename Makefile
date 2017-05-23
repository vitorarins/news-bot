IMAGE = news-bot
RUN = docker run --rm -it --net=host -v `pwd`:/app/ $(IMAGE)

guard-%:
	@ if [ "${${*}}" = "" ]; then \
                echo "Variable '$*' not set"; \
                exit 1; \
        fi

image:
	docker build -t $(IMAGE) .

run: image
	$(RUN) sh
