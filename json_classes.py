import json
class Instrument:
    def __init__(self, name, type, material):
        self.name = name
        self.type = type
        self.material = material

    def __str__(self):
        return f'{self.name} is a {self.type} instrument made of {self.material}'

    def serialize(self):
        with open(self.name + '.json', 'w') as f:
            instrument_dict = {
                'name': self.name,
                'type': self.type,
                'material': self.material
            }
            f.write(json.dumps(instrument_dict, indent=2))
            f.close()

    def load_from_file(file_name):
        with open(file_name + '.json', 'r') as f:
            instrument_dict = json.loads(f.read())
            return Instrument(instrument_dict['name'], instrument_dict['type'], instrument_dict['material'])


guitar = Instrument('Guitar', 'String', 'Mahogany')
guitar.serialize()

another_guitar = Instrument.load_from_file('Guitar')
print(another_guitar)
print(guitar)
print('Change some stuff and...')
another_guitar.name = 'Axe'
print(another_guitar)
print(guitar)