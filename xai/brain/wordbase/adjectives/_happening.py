

#calss header
class _HAPPENING():
	def __init__(self,): 
		self.name = "HAPPENING"
		self.definitions = [u'A happening place is extremely fashionable and exciting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
