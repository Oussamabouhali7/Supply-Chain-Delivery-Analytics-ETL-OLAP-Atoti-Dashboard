# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 19:02:50 2021

@author: asus
"""

import pygrametl
import psycopg2
from pygrametl.tables import Dimension,FactTable
from pygrametl.datasources import CSVSource

print("eee")
pgconn=psycopg2.connect(dbname='LIvraison',user='postgres',password='oussama938',port=5432)
connection=pygrametl.ConnectionWrapper(pgconn)
connection.setasdefault()
connection.execute('set search_path to "Livraison"')
print("OK")
#2éme etape-> modéle logique
Fournisseur_dim=Dimension(name="Fournisseur",key="id_fournisseur",attributes=["NomFournisseur","AddressFournisseur"])
Temps_dim=Dimension(name="Temps",key="id_temps",attributes=["DateLivraison","TempsLivraison"])
Chemin_dim=Dimension(name="Chemin",key="id_chemin",attributes=["id_pays","nom_pays","id_paysLivraison","nom_paysLivraison"])
Livraison_Fact=FactTable(name="Livraison",keyrefs=["id_fournisseur","id_temps","id_chemin"],measures=["qte","prix_commande"])

fichier=open("C:/Users/asus/Desktop/projetpython_oussamabouhali_ellahkaamine/projetpython_ETL/projetpython.csv","r",encoding="utf-8")
print("OK1")
LivraisonSource=CSVSource(fichier,delimiter=";")
print("OK2")

for row in LivraisonSource:
    #table Fournisseur
    row["id_fournisseur"]=row["NomFournisseur"]+":"+row["AddressFournisseur"]
    Fournisseur_dim.ensure(row)
    
    #table Temps
    row["id_temps"]=row["DateLivraison"]+"  :  "+row["TempsLivraison"]
    row["dateLivraison"]=row["DateLivraison"]
    row["tempsLivraison"]=row["TempsLivraison"]
    Temps_dim.ensure(row)
    
    #table Chemin
    row["id_chemin"]=row["id_pays"]+":"+row["nom_pays"]+"->"+row["id_paysLivraison"]+":"+row["nom_paysLivraison"]
    row["id_pays"]=row["id_pays"]
    row["nom_pays"]=row["nom_pays"]
    row["id_paysLivraison"]=row["id_paysLivraison"]
    row["nom_paysLivraison"]=row["nom_paysLivraison"]
    Chemin_dim.ensure(row)
    
    #table fait Livraison
    row["id"]=row["id"]
    row["qte"]=pygrametl.getint(row["Qte"])
    row["prix_commande"]=pygrametl.getfloat(row["PrixCommande"])
    Livraison_Fact.ensure(row)
    
connection.commit()
connection.close()
pgconn.close()

    
