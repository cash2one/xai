

#calss header
class _PANCREATIC():
	def __init__(self,): 
		self.name = "PANCREATIC"
		self.definitions = [u'relating to the pancreas (= the organ in the body that produces insulin): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
