

#calss header
class _FINANCIAL():
	def __init__(self,): 
		self.name = "FINANCIAL"
		self.definitions = [u'relating to money or how money is managed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
