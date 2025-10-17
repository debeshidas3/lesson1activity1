import random, math

angle = random.uniform(0, 360)
rad = math.radians(angle)
sinv, cosv = math.sin(rad), math.cos(rad)
tanv = math.tan(rad) if abs(cosv) > 1e-9 else float('inf')

print(f"{angle:.2f}° → sin={sinv:.4f}, cos={cosv:.4f}, tan={tanv:.4f}")
