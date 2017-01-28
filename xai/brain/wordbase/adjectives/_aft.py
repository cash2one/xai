

#calss header
class _AFT():
	def __init__(self,): 
		self.name = "AFT"
		self.definitions = [u'in or towards the back part of a boat']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
