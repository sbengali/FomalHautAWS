import boto3
import json
from boto.s3.connection import S3Connection

if __name__ == "__main__":
    conn = S3Connection()
    bucket = conn.lookup('facial-recognition-pune')
    for obj in bucket.list():
        if obj.key.endswith('.jpg'):
            fileName = obj.key
            client = boto3.client('rekognition')

            response = client.detect_faces(Image={'S3Object': {'Bucket': 'facial-recognition-pune', 'Name': fileName}}, Attributes=['ALL'])

            print('Detected faces for ' + fileName)
            for faceDetail in response['FaceDetails']:
                print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])
                      + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
                print('Here are the other attributes:')
                print(json.dumps(faceDetail, indent=4, sort_keys=True))
