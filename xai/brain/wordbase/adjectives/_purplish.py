

#calss header
class _PURPLISH():
	def __init__(self,): 
		self.name = "PURPLISH"
		self.definitions = [u'almost purple in colour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
