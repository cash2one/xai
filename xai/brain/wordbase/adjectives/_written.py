

#calss header
class _WRITTEN():
	def __init__(self,): 
		self.name = "WRITTEN"
		self.definitions = [u'expressed in writing, or involving writing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
