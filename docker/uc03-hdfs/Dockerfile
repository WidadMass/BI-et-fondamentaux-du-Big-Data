FROM apache/hadoop:3.5.0

ENV HADOOP_HOME=/opt/hadoop \
    HADOOP_CONF_DIR=/opt/hadoop/etc/hadoop \
    PATH=/opt/hadoop/bin:/opt/hadoop/sbin:$PATH

COPY core-site.xml hdfs-site.xml /opt/hadoop/etc/hadoop/
COPY entrypoint.sh /entrypoint.sh

EXPOSE 9870 9864 9000
ENTRYPOINT ["bash", "/entrypoint.sh"]
