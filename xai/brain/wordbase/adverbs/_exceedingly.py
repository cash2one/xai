

#calss header
class _EXCEEDINGLY():
	def __init__(self,): 
		self.name = "EXCEEDINGLY"
		self.definitions = [u'to a very great degree: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
