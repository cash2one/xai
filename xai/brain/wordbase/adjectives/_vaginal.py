

#calss header
class _VAGINAL():
	def __init__(self,): 
		self.name = "VAGINAL"
		self.definitions = [u'relating to the vagina (= the opening passage that leads from the vulva to the cervix): ', u'relating to a structure in the body that is shaped like a long close-fitting covering']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
