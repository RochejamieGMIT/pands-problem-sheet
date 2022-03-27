# bmi.py
# Programme to calculate bmi
# Author: Jamie Roche 
# BMI formula taken from
# Ref: https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_1.html#:~:text=With%20the%20metric%20system%2C%20the,by%2010%2C000%2C%20can%20be%20used.


weight = int(input("Enter your weight(kg)")) #Read in the weight from the user
height = int(input("Enter your height(cm)")) #Read in the height from the user

bmi = (weight/(height**2))*10000 # Using the BMI formula calculate the BMI 

print("Your BMI is {:.1f}" .format(bmi)) # Print out the BMI 