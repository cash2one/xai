

#calss header
class _INDIVIDUAL():
	def __init__(self,): 
		self.name = "INDIVIDUAL"
		self.definitions = [u'existing and considered separately from the other things or people in a group: ', u'given to or relating to a single, separate person or thing: ', u'belonging or relating to, or suitable for, people or things that are different or particular in some way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
