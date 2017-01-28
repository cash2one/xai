

#calss header
class _WAKEFUL():
	def __init__(self,): 
		self.name = "WAKEFUL"
		self.definitions = [u'not able to sleep, or used to describe a period of time when you are not able to sleep: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
