

#calss header
class _WORKING():
	def __init__(self,): 
		self.name = "WORKING"
		self.definitions = [u'relating to work: ', u'having work: ', u'operating: ', u'The working parts of a machine are those that move and make it work: ', u'used to refer to a plan, idea, or knowledge that is not complete but is good enough to be useful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
