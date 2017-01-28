

#calss header
class _PORTENTOUS():
	def __init__(self,): 
		self.name = "PORTENTOUS"
		self.definitions = [u'too serious and trying to be very important: ', u'Portentous events, statements, or signs are important because they show that something unpleasant is very likely to happen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
