

#calss header
class _DEVOUT():
	def __init__(self,): 
		self.name = "DEVOUT"
		self.definitions = [u'believing strongly in a religion and obeying all its rules or principles: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
