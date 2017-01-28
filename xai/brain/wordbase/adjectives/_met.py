

#calss header
class _MET():
	def __init__(self,): 
		self.name = "MET"
		self.definitions = [u'informal for  meteorological ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
