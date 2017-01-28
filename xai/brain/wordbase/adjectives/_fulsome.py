

#calss header
class _FULSOME():
	def __init__(self,): 
		self.name = "FULSOME"
		self.definitions = [u'expressing a lot of admiration or praise for someone, often too much, in a way that does not sound sincere: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
