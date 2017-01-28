

#calss header
class _ELATED():
	def __init__(self,): 
		self.name = "ELATED"
		self.definitions = [u'extremely happy and excited, often because something has happened or been achieved: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
