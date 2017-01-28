

#calss header
class _KEY():
	def __init__(self,): 
		self.name = "KEY"
		self.definitions = [u'very important and having a lot of influence on other people or things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
