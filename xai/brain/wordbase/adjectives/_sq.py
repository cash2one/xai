

#calss header
class _SQ():
	def __init__(self,): 
		self.name = "SQ"
		self.definitions = [u'written abbreviation for  square noun , in measurements of length']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
