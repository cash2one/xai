

#calss header
class _INDICATIVE():
	def __init__(self,): 
		self.name = "INDICATIVE"
		self.definitions = [u'being or relating to a sign that something exists, is true, or is likely to happen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
