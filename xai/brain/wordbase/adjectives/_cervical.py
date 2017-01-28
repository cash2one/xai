

#calss header
class _CERVICAL():
	def __init__(self,): 
		self.name = "CERVICAL"
		self.definitions = [u'relating to the cervix (= the narrow, lower part of the uterus): ', u'relating to the cervical vertebrae (= the bones in the neck): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
