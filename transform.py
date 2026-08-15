def textToNumber(text: str, alp: str) -> int:
    result = 0
    revText = text[::-1]
    for i in range(len(text)):
        result += alp.index(revText[i]) * len(alp) ** i
    return result

def numberToText(number: int, alp: str) -> str:
    result = ""
    while number:
        result = alp[number % len(alp)] + result
        number //= len(alp)
    return result
