

#calss header
class _PREDICTIVE():
	def __init__(self,): 
		self.name = "PREDICTIVE"
		self.definitions = [u'relating to the ability to predict: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
