

#calss header
class _OVERWROUGHT():
	def __init__(self,): 
		self.name = "OVERWROUGHT"
		self.definitions = [u'in a state of being upset, nervous, and worried: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
