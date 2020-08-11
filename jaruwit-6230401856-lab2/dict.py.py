contract = {
    "Jane Doe": "+27 555 5367",
    "John Smith": "+27 555 6254",
    "Bob Stone": "+27 555 5689"
}
contract["Jane Doe"] = "+27 555 1024"
contract["Anna cooper"] = "+27 555 3237"
print("Bob contract is", contract["Bob Stone"])
if "Bob Stone" in contract:
    print("", contract["Bob Stone"])
print(contract.keys())
print(contract.values())
