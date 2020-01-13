def calculate_bmi(height,weight):
    if not(height.isnumeric()) or not(weight.isnumeric()):
        return
    elif height=='0':
        return
    elif int(height)<0 or int(weight)<0:
        return

    BMI = int(weight) / (int(height) * int(height))
    return int(BMI)

def bmi_check(BMI):
    if BMI==None:
        return 'wrong input'
    elif BMI<18.5:
        return 'Underweight'
    elif 18.5<BMI<24.9:
        return 'OK'
    elif 25<BMI<29.9:
        return 'overweight'
    elif 30<BMI<34.9:
        return 'obesity'
    elif 35<BMI:
        return 'Severe obesity'


weight=input("enter your weight")
height=input("enter your height")
BMI=calculate_bmi(height,weight)
print(bmi_check(BMI))


