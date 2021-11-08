def medians(nums1,nums2):
    if nums1 == '[]':
        N2 = nums2[1:-1]
        F2 = (N2.split(','))
        i = iter(F2)
        B2 = list(iter(lambda: float(next(i)), None))
        n = len(B2)
        index = n//2
        if n%2:
            Q = sorted(B2)[index]
            return f"{Q:.{5}f}"
        Q1 = sum(sorted(B2)[index-1:index+1])/2
        return f"{Q1:.{5}f}"
    elif nums2 == '[]':
        N1 = nums1[1:-1]
        F1 = (N1.split(','))
        i = iter(F1)
        B1 = list(iter(lambda: int(next(i)), None))
        n = len(B1)
        index = n//2
        if n%2:
            Q = sorted(B1)[index]
            return f"{Q:.{5}f}"
        Q1 = sum(sorted(B1)[index-1:index+1])/2
        return f"{Q1:.{5}f}"
    else:
        N1 = nums1[1:-1]
        F1 = (N1.split(','))
        i = iter(F1)
        B1 = list(iter(lambda: int(next(i)), None))
        N2 = nums2[1:-1]
        F2 = (N2.split(','))
        i = iter(F2)
        B2 = list(iter(lambda: int(next(i)), None))
        S=[]
        for i in range (len(B1)):
            S.append(B1[i])
        for j in range (len(B2)):
            S.append(B2[j])
        n = len(S)
        index = n//2
        if n%2:
            Q = sorted(S)[index]
            return f"{Q:.{5}f}"
        Q1 = sum(sorted(S)[index-1:index+1])/2
        return f"{Q1:.{5}f}"


print ('Список вводится, начиная со знака [ и заканчивая знаком ], через запятую, без пробелов')
nums1 = input('nums1 = ', )
nums2 = input('nums2 = ', )
print(medians(nums1,nums2))
