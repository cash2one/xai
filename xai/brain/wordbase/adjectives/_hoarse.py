

#calss header
class _HOARSE():
	def __init__(self,): 
		self.name = "HOARSE"
		self.definitions = [u'(of a voice or a person) having a rough voice, often because of a sore throat or a cold: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
