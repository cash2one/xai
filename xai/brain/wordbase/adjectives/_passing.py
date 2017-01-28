

#calss header
class _PASSING():
	def __init__(self,): 
		self.name = "PASSING"
		self.definitions = [u'moving past: ', u'lasting only for a short time and not important or complete: ', u'used to refer to a period of time that is going past: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
