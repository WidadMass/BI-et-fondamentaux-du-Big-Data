#!/usr/bin/env bash
set -euo pipefail

mkdir -p /data/namenode /data/datanode

if [ ! -f /data/namenode/current/VERSION ]; then
  hdfs namenode -format -force -nonInteractive
fi

hdfs namenode &
NAMENODE_PID=$!

until hdfs dfs -ls / >/dev/null 2>&1; do
  sleep 2
done

hdfs datanode &
DATANODE_PID=$!

trap 'kill "$NAMENODE_PID" "$DATANODE_PID" 2>/dev/null || true' SIGTERM SIGINT
wait -n "$NAMENODE_PID" "$DATANODE_PID"
