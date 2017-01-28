

#calss header
class _HONORARY():
	def __init__(self,): 
		self.name = "HONORARY"
		self.definitions = [u'(especially of a degree) given as an honour to someone who has not done a course of study: ', u'An honorary position in an organization is one for which no payment is made: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
