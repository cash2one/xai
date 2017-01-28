

#calss header
class _MENTAL():
	def __init__(self,): 
		self.name = "MENTAL"
		self.definitions = [u'relating to the mind, or involving the process of thinking: ', u'crazy']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
