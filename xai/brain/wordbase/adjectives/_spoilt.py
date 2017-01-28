

#calss header
class _SPOILT():
	def __init__(self,): 
		self.name = "SPOILT"
		self.definitions = [u'another word for  spoiled ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
