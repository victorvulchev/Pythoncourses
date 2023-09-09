month = input()
nights = float(input())
studio_Cost = 0
appartment_Cost = 0
#May, June, July, August, September или October. 
if month == "May" or month == "October":
    studio_Cost = 50
    appartment_Cost = 65
elif month == "June" or month == "September":
    studio_Cost = 75.20
    appartment_Cost = 68.70
else:
    studio_Cost = 76
    appartment_Cost = 77

studio_Stay = nights * studio_Cost
appartment_Stay = nights * appartment_Cost

if (nights > 7 and nights <= 14) and (month == "May" or month == "October"):
    studio_Stay *= 0.95
elif nights > 14 and (month == "May" or month == "October"):
    studio_Stay *= 0.70
elif nights > 14 and (month == "June" or month == "September"):
    studio_Stay *= 0.80

if nights > 14:
    appartment_Stay *= 0.90

print(f"Apartment: {appartment_Stay:.2f} lv.")
print(f"Studio: {studio_Stay:.2f} lv.")
