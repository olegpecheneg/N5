def medians(nums1, nums2):
    num_total = nums1 + nums2
    num_total = sorted(num_total)
    lenght = len(num_total)
    if lenght == 0:
        print('ашипка')
        
    elif lenght == 1:
        a = num_total[0]
        print(float(a))
        
    elif lenght % 2 == 0:
        b1 = num_total[lenght // 2 - 1]
        b2 = num_total[lenght // 2]
        b = (b1 + b2) / 2
        print(float(b))
        
    elif lenght % 2 == 1:
        c = num_total[lenght // 2]
        print(float(c))
