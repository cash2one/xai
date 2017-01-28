

#calss header
class _COCKY():
	def __init__(self,): 
		self.name = "COCKY"
		self.definitions = [u'used to describe a young person who is confident in a way that is unpleasant and sometimes rude: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
