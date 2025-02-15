FROM alpine

RUN apk add --update --no-cache python3 py-pip bash npm

RUN mkdir -p /icarus-server/httpmitm
COPY requirements.txt /icarus-server/
COPY entry.sh /icarus-server/
COPY httpmitm /icarus-server/httpmitm
RUN pip3 install -U -r /icarus-server/requirements.txt --break-system-packages
RUN cd /icarus-server/httpmitm ; npm install
EXPOSE 8126
ENTRYPOINT ["/icarus-server/entry.sh"]
