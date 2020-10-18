print("hello! I am here to help you to select good brands in skincare prouducts")
dict={"face wash" :["plum","mama earth","good vibes","aroma majic","himalaya"],"moisturizer" :["nivea","cetaphil","The face shop","biotique","clinique"],"toner" :["kama ayurveda","good vibes","plum","wow skin sciences"],"serum" :["Mcaffeine","kiehl's","estee lauder","Dot and key","st.botanica"],"scrub" :["biotique","joy","good vibes","neutrogena","Mcaffeine"],"face mask" :["good vibes","biotique","plum","mama earth","Mcaffeine"],"night cream" :["plum","good vibes","garnier","Mcaffeine","Loreal paris"],"sunscreen" :["neutrogena","lotus","solasafe","kielh's","La shield"],"Essential oil" :["good vibes","aroma magic","nykaa","Inatur","The beauty co."],"sheet mask" :["The face shop","innisfree","garnier","nykaa","good vibes"]}
output_dict={}
count=1
print("we have amazing budget friendly brands for you")
for key in dict:
    print(count,".",key)
    count+=1
count=1
for dict_key,dict_values in dict.items():
    output_dict[count]=dict_values
    count+=1
print("please select your requirement,we have required prouducts for you")
user_input=int(input())
count=1
for key in output_dict[user_input]:
    print(count,".",key)
    count+=1
print("Thank you!")

