

#calss header
class _DISJOINTED():
	def __init__(self,): 
		self.name = "DISJOINTED"
		self.definitions = [u'(especially of words or ideas) not well connected or well ordered: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
