

#calss header
class _MINOR():
	def __init__(self,): 
		self.name = "MINOR"
		self.definitions = [u'having little importance, influence, or effect, especially when compared with other things of the same type: ', u'belonging or relating to a musical scale that is generally thought to have a sad sound: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
