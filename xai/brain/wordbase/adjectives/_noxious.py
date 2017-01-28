

#calss header
class _NOXIOUS():
	def __init__(self,): 
		self.name = "NOXIOUS"
		self.definitions = [u'Something, especially a gas or other substance, that is noxious is poisonous or very harmful: ', u'harmful and unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
