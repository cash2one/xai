

#calss header
class _UNSOLD():
	def __init__(self,): 
		self.name = "UNSOLD"
		self.definitions = [u'not sold: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
