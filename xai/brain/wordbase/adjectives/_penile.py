

#calss header
class _PENILE():
	def __init__(self,): 
		self.name = "PENILE"
		self.definitions = [u'relating to the penis']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
