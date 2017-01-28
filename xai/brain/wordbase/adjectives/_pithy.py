

#calss header
class _PITHY():
	def __init__(self,): 
		self.name = "PITHY"
		self.definitions = [u'(of speech or writing) expressing an idea cleverly in a few words: ', u'with a lot of pith: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
