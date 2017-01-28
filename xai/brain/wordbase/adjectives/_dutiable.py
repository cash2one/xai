

#calss header
class _DUTIABLE():
	def __init__(self,): 
		self.name = "DUTIABLE"
		self.definitions = [u'If good are dutiable, duty must be paid on them.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
