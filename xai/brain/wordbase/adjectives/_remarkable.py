

#calss header
class _REMARKABLE():
	def __init__(self,): 
		self.name = "REMARKABLE"
		self.definitions = [u'unusual or special and therefore surprising and worth mentioning: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
