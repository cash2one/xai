

#calss header
class _POSSESSED():
	def __init__(self,): 
		self.name = "POSSESSED"
		self.definitions = [u'to own something or have something as a quality: ', u'Someone who is possessed is thought to be controlled by an evil spirit.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
