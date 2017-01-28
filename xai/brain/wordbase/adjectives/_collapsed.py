

#calss header
class _COLLAPSED():
	def __init__(self,): 
		self.name = "COLLAPSED"
		self.definitions = [u'A collapsed lung or blood vessel (= tube that carries blood in the body) is not able to work because disease or injury has caused it to become flat.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
