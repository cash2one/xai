

#calss header
class _ULTIMATE():
	def __init__(self,): 
		self.name = "ULTIMATE"
		self.definitions = [u'most extreme or important because either the original or final, or the best or worst: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
