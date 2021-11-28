# Name: Numaan Qureshi
# Email: numaan.qureshi58@myhunter.cuny.edu
# Date: September 30 2021
# This program creates influencer tiers.

followers = input("How many social media followers do you have?: ")
a = int(followers)

if a < 0:
    b = "Error"
elif a < 1000:
    b = "Hyper Influencer"
elif 1000 <= a < 10000:
    b = "Nano Influencer"
elif 10000 <= a < 100000:
    b = "Micro Influencer"
elif 100000 <= a < 500000:
    b = "Mid-Tier Influencer"
elif 500000 <= a < 1000000:
    b = "Macro-Influencer"
elif a >= 1000000:
    b = "Celebrity Influencer"

print("Your influencer tier is:", b)

# END
