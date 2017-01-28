

#calss header
class _SUPERANNUATED():
	def __init__(self,): 
		self.name = "SUPERANNUATED"
		self.definitions = [u'old, and almost no longer suitable for work or use']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
