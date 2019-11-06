def r(n,mood):
    # print(mood)
    n=int(n)
    num=0
    from random import randint
    song_list=[]
    i=0
    if(mood=='happy' or mood=='sad' or mood=='indie' or mood=='romantic'):
        # print('')
        if(mood=='happy'):
            f_happy=open("Happy.txt",'r+')
            while i<n:
                j=f_happy.readlines()
                for k in j:
                    if(randint(-1,2)==0):
                        pass
                    else:
                        song_list.append(k)
                        i=i+1
                    if(i<n):
                        pass
                    else:
                        break
            #print(song_list)
            # for l in song_list:
            #     num=num+1
            #     print(num,":",l)
        elif(mood=='sad'):
            f_sad=open("Sad.txt",'r+')
            while i<n:
                j=f_sad.readlines()
                for k in j:
                    if(randint(-1,2)==0):
                        pass
                    else:
                        song_list.append(k)
                        i=i+1
                    if(i<n):
                        pass
                    else:
                        break
            #print(song_list)
            # for l in song_list:
            #     num=num+1
            #     print(num,":",l)
        elif(mood=='romantic'):
            f_romantic=open("Romantic.txt",'r+')
            while i<n:
                j=f_romantic.readlines()
                for k in j:
                    if(randint(-1,2)==0):
                        pass
                    else:
                        song_list.append(k)
                        i=i+1
                    if(i<n):
                        pass
                    else:
                        break
            #print(song_list)
            # for l in song_list:
            #     num=num+1
            #     print(num,":",l)
        elif(mood=='indie'):
            f_Indie=open("Indie.txt",'r+')
            while i<n:
                j=f_Indie.readlines()
                for k in j:
                    if(randint(-1,2)==0):
                        pass
                    else:
                        song_list.append(k)
                        i=i+1
                    if(i<n):
                        pass
                    else:
                        break
        return song_list

    else:
        return 'false'                
        

            
                
                
            
            