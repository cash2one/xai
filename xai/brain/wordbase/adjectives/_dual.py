

#calss header
class _DUAL():
	def __init__(self,): 
		self.name = "DUAL"
		self.definitions = [u'with two parts, or combining two things: ', u'two sets of controls in a car, one for the person who is learning to drive and one for the teacher', u'the nationality of two countries at the same time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
