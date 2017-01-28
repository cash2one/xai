

#calss header
class _INCENDIARY():
	def __init__(self,): 
		self.name = "INCENDIARY"
		self.definitions = [u'designed to cause fires: ', u'likely to cause violence or strong feelings of anger: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
