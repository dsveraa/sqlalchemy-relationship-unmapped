from models import Address, session, User

# creating users
user1 = User(name="David Vera", age=39)
user2 = User(name="Alejandra Saldaña", age=39)

# creating addresses
address1 = Address(city="Temuco", state="Araucacía", zip_code="654321")
address2 = Address(city="Chillán", state="Ñuble", zip_code="456123")
address3 = Address(city="Santiago", state="RM", zip_code="7810000")

# associating addresses with users
user1.addresses.extend([address2, address3])
user2.addresses.append(address1)

# adding users and addresses to the session and commiting changes to the database
session.add(user1)
session.add(user2)
session.commit()

print(f"{user1.addresses = }")
print(f"{user2.addresses = }")

print(f"{address1.user = }") # access user related to an address
