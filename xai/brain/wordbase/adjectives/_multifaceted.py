

#calss header
class _MULTIFACETED():
	def __init__(self,): 
		self.name = "MULTIFACETED"
		self.definitions = [u'having many different parts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
