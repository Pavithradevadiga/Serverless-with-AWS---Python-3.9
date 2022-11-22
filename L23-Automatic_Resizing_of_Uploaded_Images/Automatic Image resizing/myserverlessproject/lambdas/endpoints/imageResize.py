from lambdas.common import API_Responses as response
from lambdas.common import S3
import filetype
import json
import PIL
from PIL import Image
from io import BytesIO


def handler(event,context):
    Records = event["Records"]
    print(Records)
    try:
        def resizeImage(bucket,file,width,height):
            print('before getimage')
            getimage = S3.get(file,bucket)
            print('getimage:',getimage)
            
            fileinfo = filetype.guess(getimage)
            mime = fileinfo.mime
            ext = fileinfo.extension
            
            if ext.lower() == 'jpg':
                ext = 'JPEG'
            
            img = Image.open(BytesIO(getimage))
            print('img',img)
            resizedImage = img.resize((width,height))
            print('resizedImage:',resizedImage)
            
            b = BytesIO()
            resizedImage.save(b,ext)
            b.seek(0)
            resizedImageBuffer = b.getbuffer().tobytes()
            
            shortFileName = file.split('/')[1]
            newFileName = 'resized/'+str(width)+'x'+str(height)+'/'+shortFileName
            print('newFileName',newFileName)
    
            response = S3.write(resizedImageBuffer,newFileName,bucket,'public-read',mime)
            print('response',response)
    
            return newFileName
        
        def recordInfo(record):
            print('inside record info')
            bucket = record['s3']['bucket']['name']
            file = record['s3']['object']['key']
            print('file:',file)
            width = 300
            height = 300
            resizedImage = resizeImage(bucket,file,width,height)
            print(resizedImage)
            
            return resizedImage

        recordInfoList = map(recordInfo, Records)
        for records in recordInfoList:
            print(records)
        response._200()
        
        
        # bucket = Records[0]['s3']['bucket']['name']
        # file = Records[0]['s3']['object']['key']
        # width = 300
        # height = 300
        # return resizeImage(bucket,file,width,height)

    except Exception as Ex:
        print('Exception ocurred',Ex)
        return response._400()

    

