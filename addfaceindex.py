def update_index(tableName,faceId, fullName):
        response = dynamodb.put_item(
        TableName=tableName,
        Item={
                'RekognitionId': {'S': faceId},
                'FullName': {'S': fullName}
                }
        )
        #print(response)
def index_faces(bucket, key, collection_id, image_id=None, attributes=(), regio>
        rekognition = boto3.client("rekognition", region)
        response = rekognition.index_faces(
                Image={
                        "S3Object": {
                                "Bucket": bucket,
                                "Name": key,
                        }
                },
                CollectionId=collection_id,
                ExternalImageId="taifur",
            DetectionAttributes=attributes,
        )
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                faceId = response['FaceRecords'][0]['Face']['FaceId']
                print(faceId)
                ret = s3.head_object(Bucket=bucket,Key=key)
                personFullName = ret['Metadata']['fullname']
                #print(ret)
                print(personFullName)
                update_index('guest_collection',faceId,personFullName)
        # Print response to console.
        #print(response)
        return response['FaceRecords']
for record in index_faces(BUCKET, KEY, COLLECTION, IMAGE_ID):
        face = record['Face']
        # details = record['FaceDetail']
        print( "Face ({}%)".format(face['Confidence']))
        print( "  FaceId: {}".format(face['FaceId']))
        print( "  ImageId: {}".format(face['ImageId']))
