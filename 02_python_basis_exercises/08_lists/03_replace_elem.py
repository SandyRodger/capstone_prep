# energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']
# energy[-1] = 'geothermal'
# print(energy)
energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']
energy.remove('fossil')
energy.append('geothermal')
print(energy)
# ['solar', 'wind', 'tidal', 'fusion', 'geothermal']