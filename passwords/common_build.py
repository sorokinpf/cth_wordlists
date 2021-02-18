month = ['Zydfhm','Atdhfkm','Vfhn','Fghtkm','Vfq','B.ym','B.km','Fduecn','Ctynz,hm','Jrnz,hm','Yjz,hm','Ltrf,hm']
seasons = ['Dtcyf','Ktnj','Jctym','Pbvf']
month_l = [m.lower() for m in month]
seasons_l = [s.lower() for s in seasons]
years = range(2017,2022)
for word in month+seasons+month_l+seasons_l:
    for year in years:
        year = str(year)
        print (word+year)
        print (year+word)
