def is_passing(score):
    return score >= 50

def grade_label(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"
    

print(is_passing(48), "grade", grade_label(48))
print(is_passing(59), "grade", grade_label(59))
print(is_passing(72), "grade", grade_label(72))
print(is_passing(89), "grade", grade_label(89))