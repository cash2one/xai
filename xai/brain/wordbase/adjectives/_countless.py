

#calss header
class _COUNTLESS():
	def __init__(self,): 
		self.name = "COUNTLESS"
		self.definitions = [u'very many, or too many to be counted: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
