scales = list(map(int,input().split()))
if all(scales[i]<scales[i+1] for i in range(len(scales)-1)):
   print("ascending")
elif all(scales[i]>scales[i+1] for i in range(len(scales)-1)):
   print("descending")
else:
   print("mixed")