

#calss header
class _WAGNERIAN():
	def __init__(self,): 
		self.name = "WAGNERIAN"
		self.definitions = [u'related to the German composer Richard Wagner or his work: ', u"similar to Wagner's work, for example because of being very dramatic: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
