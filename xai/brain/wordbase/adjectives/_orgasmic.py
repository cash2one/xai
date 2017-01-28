

#calss header
class _ORGASMIC():
	def __init__(self,): 
		self.name = "ORGASMIC"
		self.definitions = [u'relating to orgasm', u'producing feelings of great pleasure or excitement: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
