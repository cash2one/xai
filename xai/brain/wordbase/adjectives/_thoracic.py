

#calss header
class _THORACIC():
	def __init__(self,): 
		self.name = "THORACIC"
		self.definitions = [u'in humans and animals, relating to chest: ', u'in insects, relating to the middle part of the body, between the head and the abdomen']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
