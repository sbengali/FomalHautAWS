import boto3

if __name__ == "__main__":

    bucket = 'facial-recognition-pune'
    targetFile = 'pic-4.jpg'
    sourceFile = 'compare-pic-1.jpg'

    client = boto3.client('rekognition')

    response = client.compare_faces(SimilarityThreshold=70,
                                  SourceImage={'S3Object':{'Bucket':bucket,'Name':sourceFile}},
                                  TargetImage={'S3Object':{'Bucket':bucket,'Name':targetFile}})

    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        confidence = str(faceMatch['Face']['Confidence'])
        print('The face at ' +
               str(position['Left']) + ' ' +
               str(position['Top']) +
               ' matches with ' + confidence + '% confidence')