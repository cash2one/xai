

#calss header
class _STOIC():
	def __init__(self,): 
		self.name = "STOIC"
		self.definitions = [u'determined not to complain or show your feelings, especially when something bad happens to you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
