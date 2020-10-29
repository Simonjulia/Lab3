Ces programmes permettent d'envoyer une liste d'entiers à un worker EC2 
qui s'occupera de réenvoyer le minimum, le maximum, la moyenne et la médiane.

Le code code_aws_stat est à placer sur le worker EC2 et à lancer 
via la commande python code_aws_stat.py

Sur le client, il faut lancer un shell python pouvant utiliser les fonctions présentes
dans client.py

La fonction envoi_liste() de client.py prend en entrée une liste d'entiers, et renvoie 
les données recues par le worker EC2.
