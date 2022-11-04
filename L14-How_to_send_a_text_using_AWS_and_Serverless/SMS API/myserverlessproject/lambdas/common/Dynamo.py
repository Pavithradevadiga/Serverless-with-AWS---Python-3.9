from distutils.log import error
import boto3

dynamodb = boto3.resource('dynamodb')


def get(ID,tableName):
    tablename = dynamodb.Table(tableName)
    

    try:
        print('inside get try')
        data = tablename.get_item(Key={'ID':ID})
        print(data['Item'])
        return data["Item"]
    except Exception as ex:
        print('exception occurred',ex) 
        raise Exception(f"There was an error fetching the data for ID of {ID} from {tableName}")

def write(data,tableName):
    tablename = dynamodb.Table(tableName)
    print(data)
    if data['ID']:

        try:
            resource =  tablename.put_item(Item = data)
            # response = tablename.put_item(Item = {'ID' :data['ID'],'datetime':data['date'],'messages':[]}) #should pass a dictionary for Item
            return data
        except Exception as ex: 
            raise Exception(f"There was an error inserting  ID of {data.ID} from {tableName}")

    else:
        raise Exception("no ID on the data")  


def delete(ID,tableName):
    tablename = dynamodb.Table(tableName)
    print(ID)
    response = tablename.delete_item(Key={'ID': ID}) 
    return response
