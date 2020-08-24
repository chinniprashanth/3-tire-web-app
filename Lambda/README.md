This lambda.py is not a part of jenkinsfile. we have to add it in aws lambda service to make it work.
It will send SNS notification once the EKS cluster is created.

       TopicArn=os.environ['email_topic'],  # Here we have to add topic arn
        Message=body,    #we can write a msg
