

#calss header
class _VOTIVE():
	def __init__(self,): 
		self.name = "VOTIVE"
		self.definitions = [u'given or done to honour and thank a god: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
