

#calss header
class _AUDIOVISUAL():
	def __init__(self,): 
		self.name = "AUDIOVISUAL"
		self.definitions = [u'used to refer to something that involves seeing and hearing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
