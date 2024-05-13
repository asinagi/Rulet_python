def ratio(first, intid):
    try:
        target_sum = first
        inputs = intid
        output = []
        #current_sum = 0
        
        # while current_sum < target_sum:
        #     value = float(input("값을 입력하세요: "))
        #     current_sum += value
        #     inputs.append(value)
        
        # if current_sum > target_sum:
        #     print("오류: 입력된 값들의 합이 목표 합을 초과했습니다.")
        #     return
        
        print("입력된 값들이 첫 번째 입력값의 몇 퍼센트인지:")
        for i, value in enumerate(inputs, start=1):
            percentage = (value / target_sum) * 100
            print(f"{i}번째 입력값: {percentage:.2f}%")
            output.append(percentage)
        print(output)
        
    except ValueError:
        print("오류: 올바른 숫자 형식이 아닙니다.")

# if __name__ == "__main__":
#     main()
