

#calss header
class _ARABLE():
	def __init__(self,): 
		self.name = "ARABLE"
		self.definitions = [u'Arable farming land is used for, or is suitable for, growing crops: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
