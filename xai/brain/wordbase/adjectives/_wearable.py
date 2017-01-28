

#calss header
class _WEARABLE():
	def __init__(self,): 
		self.name = "WEARABLE"
		self.definitions = [u'Clothes that are wearable are easy to wear because they are comfortable, acceptable in most social situations, and look attractive in combination with other clothes: ', u'Wearable technology consists of things that can be worn, such as clothing or glasses, that contain computer technology or have the ability to connect to the internet: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
