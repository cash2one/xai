

#calss header
class _SHEEPISH():
	def __init__(self,): 
		self.name = "SHEEPISH"
		self.definitions = [u'embarrassed because you know that you have done something wrong or silly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
