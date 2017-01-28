

#calss header
class _INBRED():
	def __init__(self,): 
		self.name = "INBRED"
		self.definitions = [u'an inbred quality or characteristic is firmly established in a person: ', u'produced by breeding between closely related plants, animals, or people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
