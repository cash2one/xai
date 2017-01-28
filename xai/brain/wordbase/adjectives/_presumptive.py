

#calss header
class _PRESUMPTIVE():
	def __init__(self,): 
		self.name = "PRESUMPTIVE"
		self.definitions = [u'believed to be something, or likely to be true, based on the information that you have: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
