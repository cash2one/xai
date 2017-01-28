

#calss header
class _ABSTEMIOUS():
	def __init__(self,): 
		self.name = "ABSTEMIOUS"
		self.definitions = [u'not doing things that give you pleasure, especially not eating good food or drinking alcohol']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
