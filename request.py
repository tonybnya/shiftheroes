"""
shiftheroes.fr API
"""
from pprint import pprint
import time
import requests

TOKEN_API = '56db7f2f82f79cbc457b7e072ecd74a1'
URL = 'https://shiftheroes.fr/api/v1/plannings'

headers = {
    'Authorization': f'Bearer {TOKEN_API}',
}

# Get the init list of all the daily plannings
init_list = requests.get(
    URL + '?type=daily',
    headers=headers
).json()

# Get a new list of all the plannings
new_list = requests.get(
    URL + '?type=daily',
    headers=headers
).json()

# Continuously check if there is a change between the two lists
while init_list == new_list:
    new_list = requests.get(
        URL + '?type=daily',
        headers=headers
    ).json()
    time.sleep(1)

# At this stage, there is a change into the list of all the plannings
print('New list available!')
print(new_list)
print()

# Get the id of the old plannings
OLD_ID = init_list[0]['id']
# Print the plannings in a neatly way
print(f'OLD PLANNINGS ID: {OLD_ID}')
print()

# Get the id of the new plannings
PLANNING_ID = new_list[0]['id']
# Print the plannings in a neatly way
print(f'NEW PLANNINGS ID: {PLANNING_ID}')
print()

# Get the list of all the shifts
# "https://shiftheroes.fr/api/v1/plannings/:planning_id/shifts"
response = requests.get(
    URL + f'/{PLANNING_ID}/shifts',
    headers=headers
)

# Print the shifts in a neatly way
shifts = response.json()
pprint(shifts)
print()

for shift in shifts:
    SHIFT_ID = shift['id']
    print(SHIFT_ID)

    # Book a shift
    response = requests.post(
        URL + f'/{PLANNING_ID}/shifts/{SHIFT_ID}/reservations',
        headers=headers
    ).json()

    print(response)
    print()
