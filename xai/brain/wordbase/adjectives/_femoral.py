

#calss header
class _FEMORAL():
	def __init__(self,): 
		self.name = "FEMORAL"
		self.definitions = [u'relating to the femur (= the long bone in the upper part of the leg): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
