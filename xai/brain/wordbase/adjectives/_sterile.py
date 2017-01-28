

#calss header
class _STERILE():
	def __init__(self,): 
		self.name = "STERILE"
		self.definitions = [u'(of a living being) unable to produce young, or (of land) unable to produce plants or crops: ', u'having no imagination, new ideas, or energy: ', u'completely clean and free from dirt and bacteria: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
