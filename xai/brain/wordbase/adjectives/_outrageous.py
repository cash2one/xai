

#calss header
class _OUTRAGEOUS():
	def __init__(self,): 
		self.name = "OUTRAGEOUS"
		self.definitions = [u'shocking and morally unacceptable: ', u'used to describe something or someone that is shocking because they are unusual or strange: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
