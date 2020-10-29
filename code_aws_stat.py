import boto3
import statistics
from random import randint


def creer_s3_file(liste,stats) :
    with open('log.txt', 'w') as f :
        f.write('Traitement de la liste : \n')
        for x in liste :
            f.write(str(x) + ' ')
        f.write('\nMinimum : ' + str(stats[0]) +'\nMaximum : ' + str(stats[1]) + '\nMoyenne : ' + str(stats[2]) + '\nMediane : ' + str(stats[3]))
        
    s3 = boto3.client('s3')
    s3.upload_file('log.txt','mybucket3131','log'+str(randint(1000000,1000000000))+'.txt')


sqs = boto3.resource('sqs')
queue1 = sqs.create_queue(QueueName='queue1', Attributes={'DelaySeconds': '1'})
queue2 = sqs.create_queue(QueueName='queue2', Attributes={'DelaySeconds': '1'})

while 1 :

    for message in queue1.receive_messages():
    
        text = message.body
        liste = text.split()
        print(liste)
        for i in range(len(liste)) :
            liste[i] = int(liste[i])

        # Calcul min, max, moyenne et mediane
        stats = [min(liste),max(liste),statistics.mean(liste),statistics.median(liste)]
            
        print(stats)

        response = queue2.send_message(MessageBody='Minimum : ' + str(stats[0]) +' Maximum : ' + str(stats[1]) + ' Moyenne : ' + str(stats[2]) + ' Mediane : ' + str(stats[3]))
        # Let the queue know that the message is processed
        message.delete()

        creer_s3_file(liste,stats)

