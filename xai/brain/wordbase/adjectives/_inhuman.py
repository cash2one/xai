

#calss header
class _INHUMAN():
	def __init__(self,): 
		self.name = "INHUMAN"
		self.definitions = [u'extremely cruel: ', u'not human in an unusual or frightening way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
