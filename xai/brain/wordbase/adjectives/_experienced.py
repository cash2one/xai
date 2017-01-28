

#calss header
class _EXPERIENCED():
	def __init__(self,): 
		self.name = "EXPERIENCED"
		self.definitions = [u'having skill or knowledge because you have done something many times: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
