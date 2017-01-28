

#calss header
class _SAID():
	def __init__(self,): 
		self.name = "SAID"
		self.definitions = [u'used before the name of a person or thing you have already mentioned: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
