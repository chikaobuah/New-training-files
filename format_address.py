def format_address(address_string):
  # Declare variables

  # Separate the address string into parts
  address_parts = []
  address_number = []
  address_street = []
  address_parts  = address_string.split()

  # Traverse through the address parts
  for address_part in address_parts:
    # Determine if the address part is the
    # house number or part of the street name
    if address_part.isnumeric():
      address_number.append(address_part) 
    else:
      address_street.append(address_part)

  # Does anything else need to be done 
  # before returning the result?
  address_number =" ".join(address_number)
  address_street =" ".join(address_street)
  
  # Return the formatted string  
  return "house number {} on street named {}".format(address_number, address_street)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
