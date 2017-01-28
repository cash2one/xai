

#calss header
class _TEPID():
	def __init__(self,): 
		self.name = "TEPID"
		self.definitions = [u'(of liquid) not very warm', u'A tepid reaction is not enthusiastic: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
