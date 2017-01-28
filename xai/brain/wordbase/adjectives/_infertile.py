

#calss header
class _INFERTILE():
	def __init__(self,): 
		self.name = "INFERTILE"
		self.definitions = [u'An infertile person, animal, or plant cannot have babies, produce young, or produce new plants: ', u'Infertile land or soil is not good enough for plants or crops to grow well there: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
