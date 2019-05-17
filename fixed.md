1 - Les composants vues s'enregistrent toujours avant l'instance dans laquelle on veut les utiliser
2 - Pour les composants dont le template est défini à l'extérieur du composant grâce à la balise <template>, 
il faut inclure le fichier dans lequel ils sont contenus à la fin du body avant le script
3 - To resolve conflicts between props and data members of the component,
    we begin names of all data members by m (onlyin case of conflicts)