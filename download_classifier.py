import boto3

BUCKET_NAME = 'flower-357'
LOCAL = './ml_aws/flowerapp/classifier/'
FILES = ['checkpoint',
         'flower_classifier.ckpt.data-00000-of-00001',
         'flower_classifier.ckpt.index',
         'flower_classifier.ckpt.meta']
s3 = boto3.resource('s3')

for FILE in FILES:
    s3.Bucket(BUCKET_NAME).download_file(FILE, LOCAL+FILE)