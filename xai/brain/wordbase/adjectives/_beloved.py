

#calss header
class _BELOVED():
	def __init__(self,): 
		self.name = "BELOVED"
		self.definitions = [u'loved very much: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
