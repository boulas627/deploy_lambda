import json
import psycopg2
import psycopg2.extras
import os

# document: https://docs.timescale.com/timescaledb/latest/tutorials/aws-lambda/continuous-deployment/

import json

def lambda_handler(event, context):
    print("Hello from Lambda!")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

    # Build a user facing knowledge base on SharePoint and document the tools and technologies for internal benefit 
    # Successfully assist the teams 
    # Improve the overall DevSecOps program at Takeda by working with different BU's by getting different security issues resolved
    # Learning new tools and technologies with the purpose of assisting DD&T and the overall Takeda organization

    # Development Items: This is about continuing to learn 

    # https://stackify.com/aws-lambda-with-python-a-complete-getting-started-guide/