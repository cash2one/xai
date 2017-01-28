

#calss header
class _FRAGMENTARY():
	def __init__(self,): 
		self.name = "FRAGMENTARY"
		self.definitions = [u'existing only in small parts and not complete: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
