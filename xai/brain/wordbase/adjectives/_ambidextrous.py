

#calss header
class _AMBIDEXTROUS():
	def __init__(self,): 
		self.name = "AMBIDEXTROUS"
		self.definitions = [u'able to use both hands equally well']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
