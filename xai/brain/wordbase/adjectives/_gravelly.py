

#calss header
class _GRAVELLY():
	def __init__(self,): 
		self.name = "GRAVELLY"
		self.definitions = [u"If a voice, especially a man's voice, is gravelly, it is low and rough.", u'like or containing gravel: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
