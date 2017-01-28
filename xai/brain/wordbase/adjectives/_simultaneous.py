

#calss header
class _SIMULTANEOUS():
	def __init__(self,): 
		self.name = "SIMULTANEOUS"
		self.definitions = [u'happening or being done at exactly the same time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
