ARG BASE_IMAGE=0.0.3
ARG ALIAS=biop/
FROM ${ALIAS}biop-vnc-base:${BASE_IMAGE} as base

#################################################################
# Container start
USER biop
WORKDIR /home/biop
ENTRYPOINT ["/usr/local/bin/jupyter"]
CMD ["lab", "--allow-root", "--ip=*", "--port=8888", "--no-browser", "--NotebookApp.token=''", "--NotebookApp.allow_origin='*'", "--notebook-dir=/home/biop"]
