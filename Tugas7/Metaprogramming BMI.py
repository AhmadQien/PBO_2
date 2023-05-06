class BMICalculator:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
    
    @property
    def bmi(self):
        return self.weight / (self.height/100)**2
    
    @property
    def status(self):
        bmi = self.bmi
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

def main():
    height = float(input("Masukkan tinggi badan (cm): "))
    weight = float(input("Masukkan berat badan (kg): "))

    person = BMICalculator(height, weight)
    print("BMI:", person.bmi)
    print("Status:", person.status)

    if person.status != "Normal":
        print("Anda perlu melakukan perubahan pada pola makan dan gaya hidup Anda.")
    else:
        print("Pertahankan gaya hidup sehat dan aktif Anda.")

if __name__ == "__main__":
    main()
