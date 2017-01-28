

#calss header
class _OBLIQUE():
	def __init__(self,): 
		self.name = "OBLIQUE"
		self.definitions = [u'having a sloping direction, angle, or position: ', u'(of an angle) either more or less than 90\xb0', u'Oblique remarks are not direct, so that the real meaning is not immediately clear: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
