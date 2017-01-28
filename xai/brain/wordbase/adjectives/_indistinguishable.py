

#calss header
class _INDISTINGUISHABLE():
	def __init__(self,): 
		self.name = "INDISTINGUISHABLE"
		self.definitions = [u'impossible to judge as being different when compared to another similar thing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
