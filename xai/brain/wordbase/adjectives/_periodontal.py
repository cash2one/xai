

#calss header
class _PERIODONTAL():
	def __init__(self,): 
		self.name = "PERIODONTAL"
		self.definitions = [u'relating to the gums (= the pink flesh in the mouth in which the teeth are fixed) and other tissues around the teeth: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
