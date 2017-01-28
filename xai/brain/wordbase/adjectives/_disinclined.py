

#calss header
class _DISINCLINED():
	def __init__(self,): 
		self.name = "DISINCLINED"
		self.definitions = [u'to not want to do something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
