

#calss header
class _SOPORIFIC():
	def __init__(self,): 
		self.name = "SOPORIFIC"
		self.definitions = [u'causing sleep or making a person want to sleep: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
