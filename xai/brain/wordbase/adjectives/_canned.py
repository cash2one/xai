

#calss header
class _CANNED():
	def __init__(self,): 
		self.name = "CANNED"
		self.definitions = [u'preserved and sold in a metal container: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
