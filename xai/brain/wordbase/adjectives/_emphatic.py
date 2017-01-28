

#calss header
class _EMPHATIC():
	def __init__(self,): 
		self.name = "EMPHATIC"
		self.definitions = [u'done or said in a strong way and without any doubt: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
