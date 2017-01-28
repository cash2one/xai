

#calss header
class _PREMEDITATED():
	def __init__(self,): 
		self.name = "PREMEDITATED"
		self.definitions = [u'(especially of a crime or something unpleasant) done after being thought about or carefully planned: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
