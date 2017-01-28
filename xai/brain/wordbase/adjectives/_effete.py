

#calss header
class _EFFETE():
	def __init__(self,): 
		self.name = "EFFETE"
		self.definitions = [u'weak and without much power: ', u'more typical of a woman than of a man']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
