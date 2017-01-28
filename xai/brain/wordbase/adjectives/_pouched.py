

#calss header
class _POUCHED():
	def __init__(self,): 
		self.name = "POUCHED"
		self.definitions = [u'used to refer to a female animal that has a pouch (= a pocket on the lower part of her body to carry and protect her young after they are born) : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
