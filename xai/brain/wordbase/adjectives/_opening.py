

#calss header
class _OPENING():
	def __init__(self,): 
		self.name = "OPENING"
		self.definitions = [u'happening at the beginning of an event or activity: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
