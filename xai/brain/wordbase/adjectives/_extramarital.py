

#calss header
class _EXTRAMARITAL():
	def __init__(self,): 
		self.name = "EXTRAMARITAL"
		self.definitions = [u'An extramarital sexual relationship is one between a married person and someone who is not their husband or wife: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
