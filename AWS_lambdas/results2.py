import json
import boto3
import xml.etree.ElementTree as ET
#serve per poter convertire le stringhe di date in oggetti datetime
from datetime import datetime

#funzione che riceve due stringhe che sono i due tempi e calcola la differenza tra i due
def getResult(partenza, arrivo):
    p = datetime.fromisoformat(partenza)
    a = datetime.fromisoformat(arrivo)
    risultato = a-p
    return str(risultato)
    

def lambda_handler(event, context):
    params = event['rawQueryString']
    
    x = str(params.split('&')[0]).split("=")[1]
    z = str(params.split('&')[1]).split("=")[1]
    z = z.replace("%20"," ")
    
    s3 = boto3.client("s3")
    try:
        response = s3.get_object(Bucket = "results-raceid", Key = x+".xml")
    except:
        return{
            'statusCode':400,
            'body':json.dumps("Non esistono risultati salvati per questa gara")
        }
    filexml = response['Body'].read().decode("utf-8")
    filen = filexml.replace('xmlns="http://www.orienteering.org/datastandard/3.0"','')
    filen = filen.replace('xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"','')
    root = ET.fromstring(filen)
    
    
    type = (params.split('&')[1]).split("=")[0]
    #differenza tra punto 7 e punto 9
    #punto 7
    if type == 'class':
        classifica = []
        
        for elem in root.findall('ClassResult'):
            if elem.find('Class/Id').text == z:

                for per in elem.findall('PersonResult'):
                    try:
                        posizione = str(per.find('Result/Position').text)
                        name = str(per.find('Person/Name/Given').text)
                        surname = str(per.find('Person/Name/Family').text)
                        partenza = str(per.find('Result/StartTime').text)
                        arrivo = str(per.find('Result/FinishTime').text)
                        status = str(per.find('Result/Status').text)
                        org = str(per.find('Organisation/Name').text)
                        
                        #non tutti hanno completato la corsa, qualora abbiano uno stato diverso da OK ritorno come risultato lo stato della corsa
                        if status == 'OK':
                            risultato = getResult(partenza, arrivo)
                        else:
                            risultato = status

                        person = {"Position": posizione, "Name":name, "Surname":surname, 'Result':risultato, 'Organisation':org}
                        classifica.append(person)
                    except:
                        continue
        file = classifica
        
        return {
            'statusCode': 200,
            'body': json.dumps(file)
        }
    #punto 9
    elif type == 'organisation':
        dict = []
        
        for cat in root.findall('ClassResult'):
            category = str(cat.find('Class/Id').text)
            for elem in cat.findall('PersonResult'):
                try:
                    name = str(elem.find('Organisation/Name').text)
                    if name == z:
                        id = str(elem.find('Person/Id').text)
                        name = str(elem.find('Person/Name/Given').text)
                        surname = str(elem.find('Person/Name/Family').text)
                        posizione = str(elem.find('Result/Position').text)
                        partenza = str(elem.find('Result/StartTime').text)
                        arrivo = str(elem.find('Result/FinishTime').text)
                        status = str(elem.find('Result/Status').text)
                        org = str(elem.find('Organisation/Name').text)
                        
                        #non tutti hanno completato la corsa, qualora abbiano uno stato diverso da OK ritorno come risultato lo stato della corsa
                        if status == 'OK':
                            risultato = getResult(partenza, arrivo)
                        else:
                            risultato = status
                            
                        event = {"Id":id, "Name":name, "Surname":surname, "Category":category, "Position":posizione, "Result":risultato}
                        dict.append(event)
                except:
                    continue
        
        return {
            'statusCode': 200,
            'body': json.dumps(dict)
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps("Errore")
        }
     
    
