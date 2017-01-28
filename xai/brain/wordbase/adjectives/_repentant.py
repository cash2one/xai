

#calss header
class _REPENTANT():
	def __init__(self,): 
		self.name = "REPENTANT"
		self.definitions = [u'feeling sorry for something that you have done']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
