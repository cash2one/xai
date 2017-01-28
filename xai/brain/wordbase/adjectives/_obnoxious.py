

#calss header
class _OBNOXIOUS():
	def __init__(self,): 
		self.name = "OBNOXIOUS"
		self.definitions = [u'very unpleasant or rude: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
