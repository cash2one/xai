

#calss header
class _MOMENTOUS():
	def __init__(self,): 
		self.name = "MOMENTOUS"
		self.definitions = [u'very important because of effects on future events: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
