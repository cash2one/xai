

#calss header
class _BIODEGRADABLE():
	def __init__(self,): 
		self.name = "BIODEGRADABLE"
		self.definitions = [u'able to decay naturally and in a way that is not harmful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
