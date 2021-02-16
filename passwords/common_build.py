month = ['Zydfhm','Atdhfkm','Vfhn','Fghtkm','Vfq','B.ym','B.km','Fduecn','Ctynz,hm','Jrnz,hm','Yjz,hm','Ltrf,hm']
seasons = ['Dtcyf','Ktnj','Jctym','Pbvf']

years = range(2017,2022)
for word in month+seasons:
    for year in years:
        year = str(year)
        print (word+year)
        print (year+word)
