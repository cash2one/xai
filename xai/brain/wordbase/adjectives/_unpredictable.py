

#calss header
class _UNPREDICTABLE():
	def __init__(self,): 
		self.name = "UNPREDICTABLE"
		self.definitions = [u'likely to change suddenly and without reason and therefore not able to be predicted (= expected before it happens) or depended on: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
