

#calss header
class _QUANTITATIVE():
	def __init__(self,): 
		self.name = "QUANTITATIVE"
		self.definitions = [u'relating to numbers or amounts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
