from bmi import calculate_bmi

weight = float(input("請輸入體重(kg)："))
height = float(input("請輸入身高(m)："))

bmi = calculate_bmi(weight, height)

print(f"BMI = {bmi:.2f}")