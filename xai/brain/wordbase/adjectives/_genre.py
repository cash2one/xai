

#calss header
class _GENRE():
	def __init__(self,): 
		self.name = "GENRE"
		self.definitions = [u'produced according to a particular model or style: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
