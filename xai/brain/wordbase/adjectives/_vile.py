

#calss header
class _VILE():
	def __init__(self,): 
		self.name = "VILE"
		self.definitions = [u'unpleasant, immoral, and unacceptable: ', u'extremely unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
