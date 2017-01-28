

#calss header
class _FURROWED():
	def __init__(self,): 
		self.name = "FURROWED"
		self.definitions = [u'a forehead (= part of the face above the eyes) that has lines in the skin, usually caused by worry']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
