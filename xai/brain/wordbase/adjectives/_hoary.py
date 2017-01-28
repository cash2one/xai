

#calss header
class _HOARY():
	def __init__(self,): 
		self.name = "HOARY"
		self.definitions = [u'very old and familiar and therefore not interesting or funny: ', u'(of a person) very old and with white or grey hair']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
