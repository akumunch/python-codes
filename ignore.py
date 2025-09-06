# # A,B= map(int,input().split())

# # if (A>=1) and (A<=20) and (B>=1) and (B<=20):
# #     if (B==3*A):
# #         print("Rain")
# #     else: 
# #         print("Dry")

# # else: 
# #     print("Exceeds")

# T= int(input())
# for i in range(T):
#     N,C= map(int, input().split()) #takes no. of cookies and no. of friends as input in one line
    
#     friends_cookies=[int(i) for i in input().split()]
#     #now friends_cookies contains the no. of cookies stored in a list
    
#     equal_check=0 #should be zero
#     lesser_check=0 #should be one
#     increment_req=0
    
#     while (equal_check==1) and (lesser_check==1):
        
#         for cookie in friends_cookies:
#             if (cookie==C):
#                 equal_check=1
#             if (cookie<C):
#                 lesser_check=1
            
#             if (equal_check==1):
#                 C+=1
#                 increment_req+=1
            
#         equal_check=0
#         lesser_check=0

#     print(increment_req)

# list=["X","Y","Unique Squirrel ID","Hectare","Shift","Date","Hectare Squirrel Number","Age","Primary Fur Color","Highlight Fur Color","Combination of Primary and Highlight Color","Color notes","Location","Above Ground Sighter Measurement","Specific Location","Running","Chasing","Climbing","Eating","Foraging","Other Activities","Kuks","Quaas","Moans","Tail flags","Tail twitches","Approaches","Indifferent","Runs from","Other Interactions","Lat/Long"]
# print(len(list))
d = {'a': 1, 'b': 2, 'c': 2}
d1 = {'state': {0: 'Alabama', 1: 'Alaska'}, 'x': {0: 139, 1: -204}, 'y': {0: -77, 1: -170}}
answer= 'Alabama'
for key,val in d1.items():
    for key1,val1 in val.items():
        if (val1==answer):
            index=key1
# index= [key for key,value in d1.items() if value==answer] 
# for
print(index)
