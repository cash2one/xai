

#calss header
class _ABNORMAL():
	def __init__(self,): 
		self.name = "ABNORMAL"
		self.definitions = [u'different from what is usual or average, especially in a way that is bad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
