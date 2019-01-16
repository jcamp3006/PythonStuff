def simple():
    print("I am a function")

simple()

def gbp_to_usd(gbp):
    usd = gbp*1.5
    return usd

usd = gbp_to_usd(5)
print(usd)

usd = gbp_to_usd(5.22)
print(usd)

usd = gbp_to_usd(50)
print(usd)
