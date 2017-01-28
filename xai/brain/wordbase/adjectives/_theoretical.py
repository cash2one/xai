

#calss header
class _THEORETICAL():
	def __init__(self,): 
		self.name = "THEORETICAL"
		self.definitions = [u'based on the ideas that relate to a subject, not the practical uses of that subject: ', u'related to an explanation that has not been proved']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
