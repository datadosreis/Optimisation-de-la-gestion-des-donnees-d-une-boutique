#Analyse des données

def analyse(df):
    print(df.shape) #Visualisation des dimensions du df
    print("\n")
    print(df.dtypes) #Visualisation des types de données du df
    print("\n")
    print(df.describe()) #Détection des outliers
    print("\n")
    print(df.isnull().sum()) #Vérification des valeurs manquantes
    print("\n")
    print(df[df.duplicated()].head()) #Détection des doublons
    print("\n")
    print(df.info) #Informations sur le df

#Vérification de l'unicité de la clé primaire

def test_cle(df,columns):
    a=df.drop_duplicates(subset=columns).shape[0]
    b=df.shape[0]
    if a==b: print("La clé est unique")
    else: print("La clé n'est pas unique")

#Rechercher des outliers via méthode de la distance interquartile

def find_outliers(v):
    Q1 = np.quantile(v, 0.25)
    Q3 = np.quantile(v,0.75)
    EIQ = Q3 - Q1
    LI = round(Q1 - (EIQ*1.5),2)
    print("La limite inférieure est de",LI,)
    LS = round(Q3 + (EIQ*1.5),2)
    print("La limite supérieure est de",LS,)
    return v.loc[(v < LI) | (v > LS)].to_frame()

#Rechercher des outliers via méthode du zscore

outliers=[]
def find_outliers_zscore(data):
    threshold=3
    mean=np.mean(data)
    std=np.std(data)
    
    for i in data:
        z_score=(i-mean) / std
        if np.abs(z_score)>threshold:
            outliers.append(i)
    return outliers