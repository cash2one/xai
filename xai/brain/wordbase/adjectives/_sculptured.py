

#calss header
class _SCULPTURED():
	def __init__(self,): 
		self.name = "SCULPTURED"
		self.definitions = [u'created as a sculpture: ', u"used to describe a part of someone's body that has a strong, smooth shape: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
