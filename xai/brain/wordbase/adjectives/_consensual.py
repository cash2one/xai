

#calss header
class _CONSENSUAL():
	def __init__(self,): 
		self.name = "CONSENSUAL"
		self.definitions = [u'with the willing agreement of all the people involved: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
