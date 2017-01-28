

#calss header
class _EXQUISITE():
	def __init__(self,): 
		self.name = "EXQUISITE"
		self.definitions = [u'very beautiful and delicate: ', u'used to describe feelings such as pleasure or pain that are extremely strong, or qualities that are extremely good; great: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
