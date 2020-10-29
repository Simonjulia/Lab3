import boto3


# En commentaire, un essai de créer et supprimer les queues pour chaque envoi afin
# que plusieurs utilisateurs puissent contacter le serveur en même temps avec des queues différentes.
#Cela n'a pas aboutit car nous n'avons pas réussi à empêcher le serveur de réutiliser les queues contenant les messages vers le client.
# Pour la suite, les queues utilisées sont queue1 et queue2 crées par le serveur.
"""
def creer_queue() :
    #Creer une queue et retourne l'url de celle-ci

    sqs = boto3.client('sqs')

    # Creer une queue non existente et dont la réponse (name2) est aussi nouvelle
    # Il ne faudrait creer qu'une seule fois la queue par client et réutiliser la même,
    # mais il faudrait utiliser une clé propre au client.
    if 'QueueUrls' in sqs.list_queues() :
        L_queues_url = sqs.list_queues()['QueueUrls']
        A = []
        for x in L_queues_url :
            A = A + [x[-6:]]

        j = randint(100000,999998)
        name1 = str(j)
        name2 = str(j +1)
        while ((name1 in A) or (name2 in A)) :
            j = randint(100000,999998)
            name1 = str(j)
            name2 = str(j +1)
    
    
        response = sqs.create_queue(QueueName=name1)

    else :
        name = str(randint(100000,999998))
        response = sqs.create_queue(QueueName=name)

    return(response['QueueUrl'])
"""


def recevoir_message() :

    # Recois les messages de la queue queue2 
    sqs = boto3.client('sqs')
    queue_url2 = sqs.get_queue_url(QueueName='queue2')['QueueUrl']

    response = sqs.receive_message(QueueUrl=queue_url2)

    while 'Messages' not in response :
        # Attend qu'un message soit présent
        queue_url2 = sqs.get_queue_url(QueueName='queue2')['QueueUrl']
        response = sqs.receive_message(QueueUrl=queue_url2)
        
    message = response['Messages'][0]['Body']

    receipt_handle = response['Messages'][0]['ReceiptHandle']

    # Supprime le message
    sqs.delete_message(QueueUrl=queue_url2,ReceiptHandle=receipt_handle)

    return(message)
    
def envoi_liste(L) :
    # Envoyer la liste L d'entiers vers le serveur

    strList = ' '.join(str(i) for i in L)
    
    sqs = boto3.client('sqs')

    queue_url = sqs.get_queue_url(QueueName='queue1')['QueueUrl']


    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=5,
        MessageBody=(strList)
    )

    # Attente message retour et affichage du message recu

    print(recevoir_message())

    
