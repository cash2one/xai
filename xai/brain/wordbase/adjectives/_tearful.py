

#calss header
class _TEARFUL():
	def __init__(self,): 
		self.name = "TEARFUL"
		self.definitions = [u'crying or likely to cry: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
