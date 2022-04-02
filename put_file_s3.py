import os
import boto3
from botocore.exceptions import ClientError
from botocore.client import Config

ACCESS_KEY_ID = 'AKIAVZ2JZZBABQOYT4PK'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'demodatalakeugb'
# BUCKET_NAME = 's3://demodatalakeugb/data/'

"""
Connect to S3 service
"""

client_s3 = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
)

"""
Upload file to S3 bucket
"""
data_folder = os.path.join(os.getcwd(), 'Out')
for file in os.listdir(data_folder):
    if not file.startswith('~'):
        try:
            print('Uloading file {0} ...'.format(file))
            client_s3.upload_file(
                os.path.join(data_folder, file),
                BUCKET_NAME,
                file
            )
        except ClientError as e:
            print('Credential is incorrect')
            print(e)
        except Exception as e:
            print(e)

print('Uploading is over ...')
"""
Download file from S3
"""
# client_s3.download_file(BUCKET_NAME, '', os.path.join('./Files Download/'))
