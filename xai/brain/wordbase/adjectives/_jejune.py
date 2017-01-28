

#calss header
class _JEJUNE():
	def __init__(self,): 
		self.name = "JEJUNE"
		self.definitions = [u'very simple or childish: ', u'boring and not interesting : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
