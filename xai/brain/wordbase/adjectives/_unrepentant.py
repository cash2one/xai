

#calss header
class _UNREPENTANT():
	def __init__(self,): 
		self.name = "UNREPENTANT"
		self.definitions = [u'not repentant (= feeling sorry for something that you have done)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
