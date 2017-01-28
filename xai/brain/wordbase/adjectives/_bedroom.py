

#calss header
class _BEDROOM():
	def __init__(self,): 
		self.name = "BEDROOM"
		self.definitions = [u'relating to sexual activity: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
