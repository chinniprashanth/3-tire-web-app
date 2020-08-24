#!/usr/bin/python3
import json
import boto3
import os
from kubernetes import client, config, utils
from kubernetes.client.rest import ApiException
def lambda_handler(event, context):
    # Configs can be set in Configuration class directly or using helper utility
    config.load_kube_config()
    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    if ret != None
        sns = boto3.client('sns')
        response = sns.publish(
        TopicArn=os.environ['email_topic'],
        Message=body,
      )
    # Print out the response
    print(response)
