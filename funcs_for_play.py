import winsound
import serial


#channel nos      = 1,2,3
#channe_threshold =30,30,30

def check_n_play_S1():
    MC_data=ser.readline()
    mc_Data=str(MC_data)
    mc_D=mc_Data[0:-1]
    u=mc_D.split(" ")
    if(len(u)>1):
        channel_no=u[0]
        channel_value=u[1]
        if(channel_no==1 and channel_value >30):
           winsound.PlaySound("Sound_1",winsound.SND_FILENAME)   

        
def check_n_play_S2():
    MC_data=ser.readline()
    mc_Data=str(MC_data)
    mc_D=mc_Data[0:-1]
    u=mc_D.split(" ")
    if(len(u)>1):
        channel_no=u[0]
        channel_value=u[1]
        if(channel_no==3 and channel_value >30):
           winsound.PlaySound("Sound_2",winsound.SND_FILENAME)

def check_n_play_S3():
    MC_data=ser.readline()
    mc_Data=str(MC_data)
    mc_D=mc_Data[0:-1]
    u=mc_D.split(" ")
    if(len(u)>1):
        channel_no=u[0]
        channel_value=u[1]
        if(channel_no==3 and channel_value >30):
           winsound.PlaySound("Sound_3",winsound.SND_FILENAME)
