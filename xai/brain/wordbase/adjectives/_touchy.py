

#calss header
class _TOUCHY():
	def __init__(self,): 
		self.name = "TOUCHY"
		self.definitions = [u'easily offended or upset: ', u'needing to be dealt with carefully: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
