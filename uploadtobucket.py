import boto3
s3 = boto3.resource('s3')
# Get list of objects for indexing
images=[('anikakarvat.jpeg','Anika Karvat'),
       ('courteneycox.jpeg','Courteney Cox'),
       ('jenniferaniston.jpeg','Jennifer Aniston'),
       ('matthewperry.jpeg','Matthew Perry'),
       ('mattleblanc.jpeg','Matt LeBlanc')
      ]
# Iterate through list to upload objects to S3   
for image in images:
   file = open(image[0],'rb')
   object = s3.Object('anika-images',image[0])
   ret = object.put(Body=file,
                   Metadata={'FullName':image[1]}
                   )
   #print(image[0])
   #print(image[1])
