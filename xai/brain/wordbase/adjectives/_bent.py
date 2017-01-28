

#calss header
class _BENT():
	def __init__(self,): 
		self.name = "BENT"
		self.definitions = [u'curved and not straight or flat: ', u'(especially of a person in a position of authority) dishonest: ', u'(especially of men) gay']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
