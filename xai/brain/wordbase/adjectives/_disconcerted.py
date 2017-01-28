

#calss header
class _DISCONCERTED():
	def __init__(self,): 
		self.name = "DISCONCERTED"
		self.definitions = [u'worried by something and uncertain: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
