

#calss header
class _PALTRY():
	def __init__(self,): 
		self.name = "PALTRY"
		self.definitions = [u'(of an amount of money) very small and of little or no value: ', u'of little quality or value: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
