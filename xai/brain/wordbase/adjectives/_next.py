

#calss header
class _NEXT():
	def __init__(self,): 
		self.name = "NEXT"
		self.definitions = [u'being the first one after the present one or after the one just mentioned: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
