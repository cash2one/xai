

#calss header
class _CORRESPONDING():
	def __init__(self,): 
		self.name = "CORRESPONDING"
		self.definitions = [u'similar to, connected with, or caused by something else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
