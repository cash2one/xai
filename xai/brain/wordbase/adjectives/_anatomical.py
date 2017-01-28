

#calss header
class _ANATOMICAL():
	def __init__(self,): 
		self.name = "ANATOMICAL"
		self.definitions = [u'relating to the scientific study and representation of the physical body and how its parts are arranged: ', u'relating to the physical structure of an animal or plant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
