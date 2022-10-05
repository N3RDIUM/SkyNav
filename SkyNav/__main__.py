# imports
import sys
import os

sys.path.append(os.path.dirname(__file__) + '/ephermis')
os.environ['SKYFIELD_DATA'] = os.path.join(os.path.dirname(__file__), 'ephermis')

# internal imports
import sky
print(sky.get_sky_schedule())
