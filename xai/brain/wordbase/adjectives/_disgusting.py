

#calss header
class _DISGUSTING():
	def __init__(self,): 
		self.name = "DISGUSTING"
		self.definitions = [u'extremely unpleasant or unacceptable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
