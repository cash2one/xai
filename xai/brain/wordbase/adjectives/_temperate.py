

#calss header
class _TEMPERATE():
	def __init__(self,): 
		self.name = "TEMPERATE"
		self.definitions = [u'(of weather conditions) neither very hot nor very cold: ', u'Temperate plants grow naturally in places where the weather is neither very hot nor very cold.', u"If someone's behaviour is temperate, it is calm and controlled."]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
