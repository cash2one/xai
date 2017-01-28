

#calss header
class _NET():
	def __init__(self,): 
		self.name = "NET"
		self.definitions = [u'left when there is nothing else to be taken away: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
