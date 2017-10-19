import boto3
import json
import glob

if __name__ == "__main__":
    for fileName in glob.glob("*.jpg"):
    #fileName = 'pic-1.jpg'
        bucket='facial-recognition-pune'
        client=boto3.client('rekognition')

        response = client.detect_faces(Image={'S3Object': {'Bucket': bucket,'Name': fileName}}, Attributes=['ALL'])

        print('Detected faces for ' + fileName)
        for faceDetail in response['FaceDetails']:
            print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])
                  + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
            print('Here are the other attributes:')
            print(json.dumps(faceDetail, indent=4, sort_keys=True))
