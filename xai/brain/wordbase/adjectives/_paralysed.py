

#calss header
class _PARALYSED():
	def __init__(self,): 
		self.name = "PARALYSED"
		self.definitions = [u'unable to move or act: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
