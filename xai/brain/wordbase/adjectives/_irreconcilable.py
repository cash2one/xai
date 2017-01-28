

#calss header
class _IRRECONCILABLE():
	def __init__(self,): 
		self.name = "IRRECONCILABLE"
		self.definitions = [u'impossible to find agreement between or with, or impossible to deal with: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
