

#calss header
class _IGNOMINIOUS():
	def __init__(self,): 
		self.name = "IGNOMINIOUS"
		self.definitions = [u'(especially of events or behaviour) embarrassing because of being a complete failure: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
