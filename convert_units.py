def convert_units(value, units_from, units_to):
    units = {'Cubic Bohr/atom': 1, 'Cubic Angstrom/atom': 0.14818,
                'Rydberg/atom' : 1, 'electron volts/atom': 13.6056,
                'Rydberg/Cubic Bohr': 1,'Gigapascals': 14720.5076}
    return value*units[units_from]/units[units_to]
