

#calss header
class _PROVINCIAL():
	def __init__(self,): 
		self.name = "PROVINCIAL"
		self.definitions = [u'relating to an area that is governed as part of a country or an empire: ', u'in or from the parts of the country that are not the capital city: ', u'having opinions and ideas that are old-fashioned and simple: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
