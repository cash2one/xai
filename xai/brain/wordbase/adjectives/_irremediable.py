

#calss header
class _IRREMEDIABLE():
	def __init__(self,): 
		self.name = "IRREMEDIABLE"
		self.definitions = [u'impossible to correct or cure: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
