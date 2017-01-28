

#calss header
class _DEFLATED():
	def __init__(self,): 
		self.name = "DEFLATED"
		self.definitions = [u'feeling less confident and positive than before: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
