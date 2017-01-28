

#calss header
class _CHIFFON():
	def __init__(self,): 
		self.name = "CHIFFON"
		self.definitions = [u'used to refer to food that is made light by adding the clear part of eggs that have been beaten: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
