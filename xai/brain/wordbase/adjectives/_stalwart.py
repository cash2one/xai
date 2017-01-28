

#calss header
class _STALWART():
	def __init__(self,): 
		self.name = "STALWART"
		self.definitions = [u'loyal, especially for a long time; able to be trusted: ', u'(especially of a person) physically strong']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
