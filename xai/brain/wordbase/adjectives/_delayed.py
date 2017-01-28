

#calss header
class _DELAYED():
	def __init__(self,): 
		self.name = "DELAYED"
		self.definitions = [u'happening at a later time than expected or intended: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
