"""
shiftheroes.fr API
"""
from pprint import pprint
import time
import requests

PLANNING_ID = 'pLf7ZY'
TOKEN_API = '56db7f2f82f79cbc457b7e072ecd74a1'
URL = 'https://shiftheroes.fr/api/v1/plannings'

headers = {
    'Authorization': f'Bearer {TOKEN_API}',
}

# Print the plannings in a neatly way
print(f'PLANNING_ID: {PLANNING_ID}')

# Get the list of all the shifts
# "https://shiftheroes.fr/api/v1/plannings/:planning_id/shifts"
response = requests.get(
    URL + f'/{PLANNING_ID}/shifts',
    headers=headers
)

# Print the shifts in a neatly way
shifts = response.json()
# pprint(plannings)

for shift in shifts:
    # pprint(shift)
    SHIFT_ID = shift['id']
    print(SHIFT_ID)

    # Book a shift
    response = requests.post(
        URL + f'/{PLANNING_ID}/shifts/{SHIFT_ID}/reservations',
        headers=headers
    ).json()

    print(response)
