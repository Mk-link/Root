# in following code problem solving is to calculate the amount of money per person

geld = 500
mostafa = 0
ahmed = 0
olga = 0

restgeld = geld % 3 #in this case restgeld is 2%
teilbaresGeld = geld - restgeld #in this case teilbaresGeld is 498
mostafa = teilbaresGeld/3
print(f"Mostafa´s Geldbeutel:"+ str(mostafa) + " Euro")
