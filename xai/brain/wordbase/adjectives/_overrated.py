

#calss header
class _OVERRATED():
	def __init__(self,): 
		self.name = "OVERRATED"
		self.definitions = [u'If something or someone is overrated, that person or thing is considered to be better or more important than they really are: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
