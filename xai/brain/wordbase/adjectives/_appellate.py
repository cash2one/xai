

#calss header
class _APPELLATE():
	def __init__(self,): 
		self.name = "APPELLATE"
		self.definitions = [u'involving an attempt to get a legal decision changed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
