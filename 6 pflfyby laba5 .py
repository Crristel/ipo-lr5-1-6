read_file = "text.txt" #присваиваем имя нашему файлу 
write_file = "output.txt"#присваиваем имя нашему файлу 
num=0 #присваиваем значение для num
with open(read_file, "r",encoding= "utf-8") as fr, open(write_file, "w", encoding= "utf-8") as fw: #открывааем файлы на чтение и запись 
   for line in fr: # пока line в файле открытом на чтение 
       num+=1 #каждый раз num увеличивается на 1
       fw.write(str(num) + '.')# записываем num с точкой после неё в другой файл 
       fw.write(line) #запись line в другой файл 
       
       
       
       
