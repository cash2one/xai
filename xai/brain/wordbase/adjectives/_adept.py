

#calss header
class _ADEPT():
	def __init__(self,): 
		self.name = "ADEPT"
		self.definitions = [u'having a natural ability to do something that needs skill: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
