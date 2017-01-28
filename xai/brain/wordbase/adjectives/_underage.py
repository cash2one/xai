

#calss header
class _UNDERAGE():
	def __init__(self,): 
		self.name = "UNDERAGE"
		self.definitions = [u'younger than the lowest age at which a particular activity is legally or usually allowed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
