

#calss header
class _PRACTICABLE():
	def __init__(self,): 
		self.name = "PRACTICABLE"
		self.definitions = [u'able to be done or put into action: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
