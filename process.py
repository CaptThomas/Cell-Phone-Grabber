import phonenumbers
from phonenumbers import carrier, PhoneNumberType, number_type
numbers = []
with open("numbers.csv") as f:
    for line in f:
        numbers.append(line.strip())
# Function to filter out landlines and keep only cell phone numbers
def filter_cellphones(phone_numbers):
    cell_phone_numbers = []
    for number in phone_numbers:
        try:
            parsed_number = phonenumbers.parse(number)
            #if carrier._is_mobile(number_type(parsed_number)):
            if number_type(parsed_number) == PhoneNumberType.MOBILE:
                cell_phone_numbers.append(number)
        except phonenumbers.NumberParseException:
            continue
    return cell_phone_numbers
# Strip out anything that isn't a number
numbers = [number.replace(" ", "").replace("-", "").replace("(", "").replace(")", "") for number in numbers]
# Add +1 to the beginning of each number
numbers = ["+1" + number for number in numbers]
matches = filter_cellphones(numbers)
print(len(matches))